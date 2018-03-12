import random
schools = ['Brown', 'Columbia', 'Cornell', 'Dartmouth', 'Harvard', 'UPenn', 'Princeton', 'Yale']
for i in range(len(schools)):
    chance = random.randint(1,10)
    if chance <= 1:
        print("Congratulations, you have been accepted to "+schools[i]+"!")
