age = int(input('What is your age\n'))
if age < 18:
    print ('You are not an adult')
elif age > 18 and age < 66:
    print ('You are an adult')
elif age > 66:
    print ('You are a senior')
else: print(error)
