


#RUN IN PYTHON2

def merge(arr,l,r,m):
	n1=m-l+1
	n2=r-m
	arr1=[]
	arr2=[]
	for i in range (l,m+1):
		arr1.append(arr[i])
	for i in range(m+1,r+1):
		arr2.append(arr[i])	


	i=0
	j=0
	k=l
	while(i<n1 and j<n2):
		if(arr1[i]<arr2[j]):
			arr[k]=arr1[i]
			i+=1
		else:
			arr[k]=arr2[j]
			j+=1
		k+=1
			
	while(i<n1):
		arr[k]=arr1[i]
		i+=1
		k+=1
	while(j<n2):
		arr[k]=arr2[j]
		j+=1
		k+=1				

	print(arr)	



def mergeSort(arr,l,r):
	if(l<r):
		m=l+((r-l)/2)
		mergeSort(arr,l,m)
		mergeSort(arr,m+1,r)
		merge(arr,l,r,m)


print ("Enter the number of elements in array") 
N=input()
print(N)
arr=[]
for i in range(N):
	print("Enter the next element of the array")
	arr.append(input())
print("Initial value of arr = " + str(arr))

l=0
r=N-1
print("Value of the array as the algorithm progresses")
mergeSort(arr,l,r)

	
