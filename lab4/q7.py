class Seven:
	def get_String(self):
		str=input("Enter a string:")
		return str

	def print_String(self,str):
		strupper=str.upper()	
		print(strupper)


sev=Seven()
str=sev.get_String()
sev.print_String(str)