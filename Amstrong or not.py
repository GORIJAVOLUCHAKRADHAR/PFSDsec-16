#program to find it is amsrtrong or not
n=int(input("Enter value"))
i=1
x=n
sum=0
'''Example153
   1 cube+5 cube +3 cube= 153
    Then it is Amstrong'''
while(i<=n):
    digit=n%10
    sum=sum+digit*digit*digit
    n//=10
if(x==sum):
    print("Amstrong")
else:
    print("Not amstrong")