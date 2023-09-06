
print("Select an operation to perform")
print("Select 1 to do addition")

print("Select 2 to do subtraction")

print("Select 3 to do multiplication")

print("Select 4 to do division")

op=int(input())

if op == 1:
    print("Enter 2 numbers")
    a=(int(input()))
    b=(int(input()))

    add=a+b
    print("Result is" , add)
    
    
elif op==2:
    print("Enter 2 numbers")
    a=(int(input()))
    b=(int(input()))

    if a>b:
        s=a-b
    else:
        s=b-a
    print("Result is" , s)


elif op==3:
    
    print("Enter 2 numbers")
    a=(int(input()))
    b=(int(input()))

    m=a*b
    print("Result is" , m)
    
elif op == 4:
    
    print("Enter 2 numbers")
    a=(int(input()))
    b=(int(input()))

    if b != 0:
        divi = a / b
        print("Result is", divi)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operation selection")
        

