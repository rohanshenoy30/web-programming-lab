class POW:
	def power(self,x,n):
		return pow(x,n)

x=int(input("enter x:"))
n=int(input("enter x:"))

pow1=POW()
answer=pow1.power(x,n)
print(answer)