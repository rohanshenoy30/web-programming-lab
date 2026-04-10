class SubsetGenerator:
    def get_subsets(self, nums):
        subsets = [[]]
        
        for n in nums:
            new_subsets = []
            for current_subset in subsets:
                new_subsets.append(current_subset + [n])
            
            subsets.extend(new_subsets)
            
        return subsets

nums=[]
size=int(input("Enter the number of elements:"))
print("Enter the elements:")
for i in range(size):
    element=int(input())
    nums.append(element)
gen = SubsetGenerator()
print(gen.get_subsets(nums))
