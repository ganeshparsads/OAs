#user inputs
ip1 = "zxyzxxyz"
ip2 = "xxzy"
p = 1

#sorting the second string
str2 = ''.join(sorted(ip2))

#length of strings
l1 = len(ip1)
l2 = len(ip2)

#output variable storing the count of return strings
count = 0

#for loop to iterate each case
for i in range(l1-(l2*p)+1+1):
    temp = [] #temp variable
    
    #making the temp variable
    for j in range(l2):
        temp.append(ip1[i + j*p])
        
    #making a sorted string out of the list
    temp = ''.join(sorted(temp))
    
    #if string is equal to given input
    if(temp == ip2):
        count+=1

#printing the output
print(count)