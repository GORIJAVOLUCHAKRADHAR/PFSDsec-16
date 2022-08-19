#program to find sum of squares of natural numbers
n=int(input("Enter number"))
s=0
i=1
while (i<=n):
    s=s+i*i
    i=i+1
print(s)