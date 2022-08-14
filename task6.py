# Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers

lst = []
tup = ()

print("Enter sequence of numbers(',' is separator; to stop entering just press Enter):")
nums = input()
lst = nums.split(",")
tup = tuple(nums.split(","))


print(f"List = {lst}" )
print(f"Tuple = {tup}")
