#simple calculator 

print ("Welcome to the Simple Calculator!")

#Get user input

num1= float(input("Enter first number: "))
num2= float(input("Enter second number: "))

#show opration choices
print("Select operation:")
print("1. Add(+)")
print("2. Subtract(-)")
print("3. Multiply(*)")
print("4. Divide(/)")  

#get user choice
choice = input("Enter choice (+,-,*,/): ")

#perform calculation

if choice == '+':
    result = num1 + num2
    print("result:", result)
elif choice == '-':
    result = num1 - num2
    print("result:", result)
elif choice == '*':
    result = num1 * num2
    print("result:", result)    
elif choice == '/': 
    if num2 != 0:
        result = num1 / num2
        print("result:", result)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid input. Please enter a valid operation (+, -, *, /).")