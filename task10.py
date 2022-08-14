#  Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.

n = input()
print(int(n) + int(str(n) + str(n)) + int( str(n) + str(n) + str(n)))
print(("%s%s" % (n,n)))
