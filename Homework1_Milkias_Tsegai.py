from rich import print

# Exercise 1

# Complete the code
m1="https://database.com/user/augustom,AugUSto Martin, 23, Approved,,"
m2="https://database.com/user/juliasch,JuLIA SchmidT, 67, rejected,,"
m3="https://database.com/user/kmarx,Karl Marx, 42, rejected,,"
m1_mod=m1.replace(" ","").removeprefix("https://database.com/user/").removesuffix(",,").lower()
m2_mod=m2.replace(" ","").removeprefix("https://database.com/user/").removesuffix(",,").lower()
m3_mod=m3.replace(" ","").removeprefix("https://database.com/user/").removesuffix(",,").lower()

print ("message: ",m1_mod)
print ("message: ",m2_mod)
print ("message: ",m3_mod)


# Exercise 2

import math

d = 9 ; #Diameter of circle
a = 45 ; #angle measure in degrees

r = d/2 ; #Radius

s = (a/360) * 2 * math.pi * r;

Arc_length = print(s)






