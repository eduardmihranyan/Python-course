from math import sqrt

def erat(n):
    """Eratosthenes algorithm to return 
    the list of all prime numbers less than n"""
    numbers=list(range(2,n))
    indx=1
    for num in numbers:
        if num>sqrt(n):
            break
        for i in numbers[indx:]:
            if i%num==0:
                numbers.remove(i)
        indx+=1
    return numbers

num=int(input("Enter a number: "))

l=erat(num)
if len(l)>5:
    print("The last five prime numbers are",l[-5:])
else:
    print("The prime numbers are",l)



