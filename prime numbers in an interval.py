#program to print prime numbers from an interval
p = int(input("Enter value"))
q = int(input("Enter value"))
for x in range(p, q + 1):
    if x > 0:
        for i in range(2,x):
            if (x % i) == 0:
                break
        else:
            print(x)
