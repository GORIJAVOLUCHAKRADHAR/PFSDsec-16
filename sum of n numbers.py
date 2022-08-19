#program to find sum of natural numbers
class Student:
    def num(self):
        print(self.value)
    n=int(input("Enter number"))
    s=0
    i=1
    while(i<=n):
        s=s+i
        i=i+1
    value=s
ob=Student()
ob.num()

#2 Second method to find sum of natuural numbers

x=int(input("Enter value"))
sum=x*(x+1)/2 #logic for x natural numbers
print(sum)