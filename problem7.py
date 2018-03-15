def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y

print('Enter a number:')
print('1. Add')
print('2. Subtract')
print('3. Multiply')
print('4. Divide')

operation = input('Choose an operation(1,2,3,4):')

if operation == '1':
    number1 = int(input('Enter the first number:'))
    number2 = int(input('Enter the second number:'))
    print(number1, '+', number2, '=', add(number1, number2))
elif operation == '2':
    number1 = int(input('Enter the first number:'))
    number2 = int(input('Enter the second number:'))
    print(number1, '-', number2, '=', subtract(number1, number2))
elif operation == '3':
    number1 = int(input('Enter the first number:'))
    number2 = int(input('Enter the second number:'))
    print(number1, '*', number2, '=', multiply(number1, number2))
elif operation == '4':
    number1 = int(input('Enter the first number:'))
    number2 = int(input('Enter the second number:'))
    print(number1, '/', number2, '=', divide(number1, number2))
else:
    print('Error')
