with open ('Prob04.in.txt') as x:
  limit = int((x.readline()))
  numbers = [0,1]
  
  
  while True:
    if len(numbers) > limit:
      break
    numbers.append(numbers[-2] + numbers[-1])
    
  for i in range(0, limit):
    v = int((x.readline()))
    print(str(v) + " = " + str(numbers[v-1]))
