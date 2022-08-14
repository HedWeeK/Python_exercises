#Write a Python program which accepts the radius of a circle from the user and compute the area.

import math

r = input('Input radius: \n')
square_r = pow(int(r), 2)
S = math.pi * float(square_r)
print(f"Area = {S}")

