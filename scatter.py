import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def create_freq_table(dataframe, stopwords=None):
    corpus = dataframe['lemmatized']
    # Tokenize corpus
    toks = corpus.str.replace(r'[^\w\s]', '').str.split().explode()
    
    if stopwords:
        toks = toks[~toks.isin(stopwords)]
    
    # Create frequency table
    frequency_table = toks.value_counts().reset_index()
    frequency_table.columns = ['feature', 'frequency']
    return frequency_table

# Importing data
df = pd.read_csv("../../data/tweets/combined_US_politician_twitter_timelines_2010-11-06_to_2022-12-31_lemma.csv.gzip", encoding="UTF-8")

# Setting stopwords
marimo = open("../../data/utilities/marimo.txt").read().splitlines()
en_stopwords = open("../../data/utilities/stopwords_en.txt").read().splitlines()
belief_speaking_df = pd.read_csv("../../data/utilities/belief_speaking_p=0.05_swapped_wn_def_example.csv")
truth_seeking_df = pd.read_csv("../../data/utilities/truth_seeking_p=0.05_swapped_wn_def_example.csv")

b_keywords = belief_speaking_df.dropna()['belief_speaking'].tolist()
t_keywords = truth_seeking_df.dropna()['truth_seeking'].tolist()

# Extracting dataframes
lemmatized_dataset = df[(df['classes_quant'] != "dn") & (df['classes_quant'] != "rn") & (~df['lemmatized'].isnull())]
belief_df = lemmatized_dataset[(lemmatized_dataset['classes_quant'] == "db") | (lemmatized_dataset['classes_quant'] == "rb")]
truth_df = lemmatized_dataset[(lemmatized_dataset['classes_quant'] == "dt") | (lemmatized_dataset['classes_quant'] == "rt")]
dem_df = lemmatized_dataset[(lemmatized_dataset['classes_quant'] == "db") | (lemmatized_dataset['classes_quant'] == "dt")]
rep_df = lemmatized_dataset[(lemmatized_dataset['classes_quant'] == "rb") | (lemmatized_dataset['classes_quant'] == "rt")]

# Creating frequency tables
tweets_freq = create_freq_table(lemmatized_dataset, marimo + en_stopwords + b_keywords + t_keywords)
b_freq = create_freq_table(belief_df, marimo + en_stopwords + b_keywords + t_keywords)
t_freq = create_freq_table(truth_df, marimo + en_stopwords + b_keywords + t_keywords)
dem_freq = create_freq_table(dem_df, marimo + en_stopwords + b_keywords + t_keywords)
rep_freq = create_freq_table(rep_df, marimo + en_stopwords + b_keywords + t_keywords)

# Calculating precision and recall values
st_df = tweets_freq.merge(b_freq, on='feature', how='left') \
                   .merge(t_freq, on='feature', how='left') \
                   .merge(dem_freq, on='feature', how='left') \
                   .merge(rep_freq, on='feature', how='left') \
                   .fillna(0)

st_df = st_df[(st_df['total_freq'] > 200)]
st_df['b_precision'] = st_df['b_freq'] / (st_df['b_freq'] + st_df['t_freq'])
st_df['b_freq_pct'] = st_df['b_freq'] / st_df['b_freq'].sum()
st_df['t_precision'] = st_df['t_freq'] / (st_df['t_freq'] + st_df['b_freq'])
st_df['t_freq_pct'] = st_df['t_freq'] / st_df['t_freq'].sum()
st_df['dem_precision'] = st_df['dem_freq'] / (st_df['dem_freq'] + st_df['rep_freq'])
st_df['dem_freq_pct'] = st_df['dem_freq'] / st_df['dem_freq'].sum()
st_df['rep_precision'] = st_df['rep_freq'] / (st_df['rep_freq'] + st_df['dem_freq'])
st_df['rep_freq_pct'] = st_df['rep_freq'] / st_df['rep_freq'].sum()

# Calculating CDF for precision and recall
for col in ['b_precision', 'b_freq_pct', 't_precision', 't_freq_pct', 'dem_precision', 'dem_freq_pct', 'rep_precision', 'rep_freq_pct']:
    st_df[col+'_cdf'] = norm.cdf(st_df[col], loc=st_df[col].mean(), scale=st_df[col].std())

# Extracting scaled F-score (harmonic mean of CDFs)
st_df['b_scaled_fscore'] = 2 * ((st_df['b_precision_cdf'] * st_df['b_freq_pct_cdf']) / (st_df['b_precision_cdf'] + st_df['b_freq_pct_cdf']))
st_df['t_scaled_fscore'] = 2 * ((st_df['t_precision_cdf'] * st_df['t_freq_pct_cdf']) / (st_df['t_precision_cdf'] + st_df['t_freq_pct_cdf']))
st_df['dem_scaled_fscore'] = 2 * ((st_df['dem_precision_cdf'] * st_df['dem_freq_pct_cdf']) / (st_df['dem_precision_cdf'] + st_df['dem_freq_pct_cdf']))
st_df['rep_scaled_fscore'] = 2 * ((st_df['rep_precision_cdf'] * st_df['rep_freq_pct_cdf']) / (st_df['rep_precision_cdf'] + st_df['rep_freq_pct_cdf']))

# Computing scaled F-score of negative scoring terms
st_df['comp_scaled_f_score'] = np.where(st_df['b_scaled_fscore'] > st_df['t_scaled_fscore'], st_df['b_scaled_fscore'], 1 - st_df['t_scaled_fscore'])
st_df['comp_scaled_f_score'] = 2 * (st_df['comp_scaled_f_score'] - 0.5)
st_df['party_scaled_f_score'] = np.where(st_df['dem_scaled_fscore'] > st_df['rep_scaled_fscore'], st_df['dem_scaled_fscore'], 1 - st_df['rep_scaled_fscore'])
st_df['party_scaled_f_score'] = 2 * (st_df['party_scaled_f_score'] - 0.5)

# Plotting results
st_df_filtered = st_df[(st_df['comp_scaled_f_score'].abs() > 0.65) | (st_df['party_scaled_f_score'].abs() > 0.65)].copy()
st_df_filtered['keyword'] = np.where((st_df_filtered['comp_scaled_f_score'].abs() > 0.65) | (st_df_filtered['party_scaled_f_score'].abs() > 0.65), st_df_filtered['feature'], "")

plt.figure(figsize=(9, 5))
plt.scatter(st_df_filtered['party_scaled_f_score'], st_df_filtered['comp_scaled_f_score'], c=st_df_filtered['party_scaled_f_score'], cmap='Rd')
