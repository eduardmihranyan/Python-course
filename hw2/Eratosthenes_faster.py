from math import sqrt

def erat(n):
    """Eratosthenes algorithm to return 
    the list of all prime numbers less than n"""
    numbers=list([True for x in range(n)])
    k=2
    while k<=sqrt(n):
        i=k**2
        while i<n:
            numbers[i]=False
            i+=k
        k+=1
    return [x for x in range(2,n) if numbers[x]]

num=int(input("Enter a number: "))

l=erat(num)
if len(l)>5:
    print("The last five prime numbers are",l[-5:])
else:
    print("The prime numbers are",l)