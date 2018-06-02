with open("Prob05.in.txt") as x:
	cases = int(x.readline().replace("\n", ""))
	for i in range(0, cases):
		num = int(x.readline().replace("\n", ""))
		temp = num
		count = 1
		while True:
			if temp == 1:
				break
			if temp % 2 == 0:
				count = count+1
				temp = int(temp/2)
			elif temp % 2 == 1:
				count = count+1
				temp = int(temp*3+1)
		print(str(num)+":"+str(count))
