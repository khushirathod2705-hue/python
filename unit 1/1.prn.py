#Write a program to input p, r, n and find out interest using simple input output statement

p = float(input ("enter principal amount: "))
r = float(input ("enter rate of interest: "))
n = float(input ("enter time: "))

si = (p * r * n) / 100

print ("simple interest =", si)
