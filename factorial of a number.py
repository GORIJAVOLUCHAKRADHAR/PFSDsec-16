#program to find the factorial of a given number
n=int(input("Enter value"))
i=1
sum=1
                                        '''for example n=5 then sum becomes 5
                                        and n becomes 4 and loop runs again till i==n
                                        so we can find the factorial of a given number'''
while(i<=n):
    sum=n*i*sum
    n=n-1
print(sum)
