import sys

def add(num1, num2):
    a = num1 + num2
    return a
def sub(num1, num2):
    s = num1 - num2
    return s
def mul(num1, num2):
    m = num1 * num2
    return m

num1 = float(sys.argv[1])
num2 = float(sys.argv[3])
operation = sys.argv[2]

if operation == "add":
    output = add(num1, num2)
    print (output)
elif operation == "mul":
    output = mul(num1, num2)
    print (output)

if operation == "sub":
    output = sub(num1, num2)
    print (output)
