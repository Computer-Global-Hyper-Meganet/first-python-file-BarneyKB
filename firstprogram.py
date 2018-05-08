firstNumber = int(input("Please input a number: "))
secondNumber = int(input("Please input another number: "))

operation = input("What would you like to do? ").lower()

if operation == "divide":
    print(firstNumber/secondNumber)
elif operation == "multiply":
    print(firstNumber*secondNumber)
elif operation == "add":
    print(firstNumber+secondNumber)
else:
    print(firstNumber-secondNumber)
