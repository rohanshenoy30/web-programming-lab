def TwoSum(arr,target):
	flag=0
	for i in range(0,len(arr)):
		for j in range(i+1,len(arr)):
			if arr[i]+arr[j]==target:
				print([i,j])
				flag=1
	if flag==0:
		print("does not exist\n")


arr=[]
num=input("enter no of numbers in the array:")

print("enter array elements:")
for i in range(int(num)):
	element=int(input())
	arr.append(element)

target=int(input("Enter the target:"))
TwoSum(arr,target)
