def add(x , y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

print("Select an  operation to perform...!")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter choice (1/2/3/4): ")

num1 =float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
    print("The Sum Is:", add(num1 , num2))

elif choice == '2':
    print("The Difference Is:", subtract(num1, num2))

elif choice == '3':
    print("The Product Is:", multiply(num1, num2))

elif choice == '4':
    print(" The Result Is:", divide(num1, num2))

else:
    print("Invalid input.please enter the valid choice!")