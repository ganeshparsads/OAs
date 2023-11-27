def checkpalindrome(string_name):
    rev=''.join(reversed(string_name))
    if(rev==string_name):
        return 1
    else:
        return 0

s="abccba"
count=0
x=[]

for i in range(len(s)+1):
    for j in range(len(s)+1):
        su=(s[i:j])
        if(checkpalindrome(su)==1):
            x.append(su)

res = []
for ele in x:
    if ele.strip():
        res.append(ele)

print(len(res))