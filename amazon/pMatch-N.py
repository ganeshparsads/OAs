from collections import deque

# ip1 = "abcbcdcadbb"
# ip2 = "abbc"
# p = 3
# op = 2

# ip1 = "acbbca"
# ip2 = "acb"
# p = 2
# op = 2

ip1 = "zxyzxxyz"
ip2 = "xxzy"
p = 1
op = 4

char_dict = {'a': 2,'b': 3, 'c': 5, 'd': 7,'e': 11, 'f': 17, 'g': 23, 'h': 29, 'i': 31,'j': 37, 'k': 41,
'l': 43,'m': 47, 'n': 53,'o': 59, 'p': 67, 'q': 71,'r': 73, 't': 61, 'u': 79, 'v': 83, 'x': 89, 'y': 97, 'z': 101,'s': 103}

ip2Prod = 1
for i in ip2:
    ip2Prod = ip2Prod * char_dict[i]

# print(ip2, ip2Prod)

n = len(ip1)
m = len(ip2)
str1 = list(ip1)
sort_ip2 = sorted(ip2)

count = 0

# tuple: (anagramProduct, letter, length of anagram)

dp = [(1, 'a', 1) for i in range(n)]


for i in range(n-1, -1, -1):
    if i == 4:
        import pdb
        pdb.set_trace()

    char = str1[i]
    if i+p > n-1:
        dp[i] = (char_dict[char], char, 1)
    elif dp[i+p][2] < m:
        anaProd, letter, lenOfAna = dp[i+p]
        anaProd = anaProd * char_dict[char]
        lenOfAna += 1
        dp[i] = (anaProd, char, lenOfAna)

        if lenOfAna == m:
            print("First Matched")
            if anaProd == ip2Prod:
                count += 1
    elif dp[i+p][2] == m:
        anaProd, letter, lenOfAna = dp[i+p]
        
        anaProd = anaProd // char_dict[letter]
        anaProd = anaProd * char_dict[char]
        dp[i] = (anaProd, char, lenOfAna)

        if len(dp[i]) == m:
            print("Matched")
            if anaProd == ip2Prod:
                count += 1

print(count)

if count == op:
    print("Working!!!")
else:
    print("Fucked up!!!")