#program to find eheter the given number is prime or not
n=int(input("Enter value"))
i=1
count=0
'''logic : if(count got incremented to more than 2 then it is composite number)
         if(count less than or equal to 2 then it is a prime number)'''
while(i<=n):
    if(n%i==0):
        count=count+1
    i=i+1
if(count==2):
    print("prime number")
else:
    print("composite number")