#Write a Python program to accept a filename from the user and print the extension of that.

import os

print("Enter filename: ")
ext_chk = os.path.splitext(input())
print(f"File extension: {ext_chk[1]}")
