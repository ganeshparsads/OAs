#First, here's  a pure list version
my_sortLambdaLst = [lambda x,y:cmp(x[0], y[0]), lambda x,y:cmp(x[1], y[1])]
def multi_attribute_sort(x,y):
    r = 0
    for l in my_sortLambdaLst:
        r = l(x,y)
        if r!=0: return r #keep looping till you see a difference
    return r

Lst = [(4, 2.0), (4, 0.01), (4, 0.9), (4, 0.999),(4, 0.2), (1, 2.0), (1, 0.01), (1, 0.9), (1, 0.999), (1, 0.2) ]
Lst.sort(lambda x,y:multi_attribute_sort(x,y)) #The Lambda of the Lambda
for rec in Lst: print str(rec)