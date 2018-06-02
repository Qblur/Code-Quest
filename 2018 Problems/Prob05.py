with open("Prob05.in.txt", "rt") as x:
    cases = int(x.readline())
    print(cases)
    for i in range(0, cases):
        current = int(x.readline())
        count = 1
        num = current
        while num != 1:
            if num % 2 == 0:
                count += 1
                num = num // 2
            elif num % 2 == 1:
                count += 1
                num = (num*3)+1
        print(str(current)+":"+str(count))
