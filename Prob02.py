with open('Prob02.in.txt') as x:
	vowels = ['a', 'e', 'i', 'o', 'u']
	cases = int(x.readline().replace("\n", ""))
	for i in range(0, cases):
		word = x.readline().replace("\n", "")
		v = 0
		for t in range(0, len(word)):
			if word[t] in vowels:
				v = v+1
		print(v)