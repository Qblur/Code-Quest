def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y

print('choose one thanks')
print('1.add')
print('2.subtract')
print('3.multiply')
print('4.divide')

operation = input('Choose an operation(1,2,3,4):')


number1 = int(input('first number'))
number2 = int(input('second number'))

if operation == '1':
    print(number1, '+', number2, '=', add(number1, number2))
elif operation == '2':
    print(number1, '-', number2, '=', subtract(number1, number2))
elif operation == '3':
    print(number1, '*', number2, '=', multiply(number1, number2))
elif operation == '4':
    print(number1, '/', number2, '=', divide(number1, number2))
if operation != (1,2,3,4):
    print('wronginput')
    
    
