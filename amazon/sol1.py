def solution(A):
	d=[]
	for i in range(len(A)-1):
		if(A[i]-A[i+1]!=0):
			d.append(A[i]-A[i+1])
	a=0
	for i in range(len(d)-1):
		if(d[i]*d[i+1]<0):
			a+=1
	a+=2
	return a

if __name__ == '__main__':
    q = [2,2,3,4,3,3,2,2,1,1,2,5]
    print(solution(q))
