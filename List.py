def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a // b


# Now we will take inputs from the user
print("Please select the operation.")
print("a. Add")
print("b. Subtract")
print("c. Multiply")
print("d. Divide")

choice = input("Please enter choice: ")

num1 = int(input(" enter the number: "))
num2 = int(input(" enter the  number: "))

if choice == 'a':
    print(add(num1, num2))

elif choice == 'b':
    print( sub(num1, num2))

elif choice == 'c':
    print(mul(num1, num2))
elif choice == 'd':
    print(div(num1, num2))
else:
    print("This is an invalid input")

