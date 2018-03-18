change = int(input('Enter change to be dispensed:'))
quarters = change // 25
change = change % 25
print(str(quarters)+" Quarters")
dimes = change // 10
change = change % 10
print(str(dimes)+" Dimes")
nickels = change // 5
change = change % 5
print(str(nickels)+" Nickels")
print(str(change)+" Pennies.")


