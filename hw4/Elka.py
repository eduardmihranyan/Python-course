def elka(n):
    """Prints Christmas tree of size n"""
    for i in range(n):
        print(" "*(n-i-1)+"* "*(i+1))
    print(" "*(n-3)+"* * *")
    print(" "*(n-3)+"* * *")
n=int(input("What size of tree would you like to see ?"))

elka(n)