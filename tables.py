#program to buit a number table
class Tables:
    n=int(input("Enter table name"))
    i=1
    while(i<=10):
        n=n*1
        print(n,'x',i,'=',n*i)
        i=i+1