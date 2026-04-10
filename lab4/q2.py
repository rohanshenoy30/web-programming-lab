class BinarySearch:
	def search(self,arr,l,r,num):
		m=(l+r)//2
		if arr[m]==num:
			print(str(num)+" found at posn "+str(m))

		elif arr[m]>num:
			self.search(arr,l,m-1,num)
		else:
			self.search(arr,m+1,r,num)




arr=[1,2,3,4,5,324,34,124,14,124]
arr.sort()
size=len(arr)
num=14
search1=BinarySearch()
search1.search(arr,0,size-1,num)

