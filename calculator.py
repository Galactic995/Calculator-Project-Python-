#A simple calculator that asks the user for inputs and uses if statements to preform operations

#asks the user to specify what operation will take place
operation = input("input operation (+, -, *, /, **, square root): ")

#asks the user for the first number for the equation
num1 = float(input("input first number: "))

#asks the user for the second number for the equation
num2 = float(input("input second number: "))

#if the user entered any form of saying add in the operation field this line of code will recognize that and add the numbers given by the user together
if operation == "+" or operation == "addition" or operation == "add":
    result = num1 + num2

#if the user entered any form of saying subtract in the operation field this line of code will recognize that and subtract the numbers given by the user together
elif operation == "-" or operation == "subtraction" or operation == "sub":
    result = num1 - num2

#if the user entered any form of saying multiply in the operation field this line of code will recognize that and multiply the numbers given by the user together
elif operation == "*" or operation == "multiplication" or operation == "mul" or operation == "multiply":
    result = num1 * num2

#if the user entered any form of saying divide in the operation field this line of code will recognize that and divide the numbers given by the user together
elif operation == "/" or operation == "division" or operation == "div" or operation == "divide":
    result = num1 / num2

#if the user entered any form of saying to the power of in the operation field this line of code will recognize that and put the first number to the power of the second number
elif operation == "**" or operation == "power" or operation == "pow":
    result = num1 ** num2

#it the user said square root into the operation field the first number will be square rooted
elif operation == "square root" or operation == "sqrt":
    result = num1 ** 0.5

#if the user puts anything other than the specified operations an error will appear
else:
    result = print("invalid operation")

#prints the result
print(result)
