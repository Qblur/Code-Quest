with open('Prob03.in.txt') as x:
    limit = int(x.readline())

    
    for i in range(0, limit):
        line = x.readline()
        a, b = line.split(' ')
        a = int(a)
        b = int(b)
        add = a + b
        mult = a * b
        out = str(add)+" "+str(mult)
        print(out)
