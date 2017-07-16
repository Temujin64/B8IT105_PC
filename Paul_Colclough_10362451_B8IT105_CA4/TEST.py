first =  input("First: ")
second =  input("Second: ")

def primeit(first, second):
	nums = range(first, second) 
	for i in range(2, 8): 
		 nums = filter(lambda x: x == i or x % i, nums)
	return nums
	
print primeit(first, second)