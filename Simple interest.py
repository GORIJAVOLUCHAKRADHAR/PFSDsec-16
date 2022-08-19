#program to find simple interest
x=int(input("Enter value"))
y=int(input("Enter value"))
z=int(input("Enter value"))
SI=(x*y*z)/100
print(SI)


#program to find com[pound interest
p=int(input("Enter value"))
r=float(input("Enter value"))
n=int(input("Enter value"))
t=int(input("Enter value"))
#Formula for compound interest   A = P*(1 + r/n)^nt
k=(1 + r/n)
b=n*t
from math import pow
c=pow(k,b)
A=p*c
print(A)