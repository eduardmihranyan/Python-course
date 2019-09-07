def add(num1,num2):
    """Adds two numbers"""
    return num1+num2
def sub(num1,num2):
    """Subtracts two numbers """
    return num1-num2
def mul(num1,num2):
    """Multiplies two numbers"""
    return num1*num2
def div(num1,num2):
    """Divides two numbers"""
    return num1/num2

ops={"+":add,"-":sub,"*":mul,"/":div}

print("Select the operation:")
print("Press + to add two numbers")
print("Press - to subtract two numbers")
print("Press * to multiply two numbers")
print("Press / to divide two numbers")


operation=input()

num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))

print(num1,operation,num2,"=", ops[operation](num1,num2),sep="")
