def average(a):
    b = a.split(",")
    num = 0
    denom = 0

    for i in range(len(b)):
        a = b[i].strip()
        if a == "K":
            denom = denom +1
        elif a == "1B":
            num = num +1
            denom = denom +1
        elif a == "2B":
            num = num + 2
            denom = denom +1
        elif a == "3B":
            num = num + 3
            denom = denom +1
        elif a == "HR":
            num = num + 4
            denom = denom +1
    if denom == 0:
        return(0.000)
    answer = num/denom
    return(answer)

with open('Prob07.in.txt') as x:
    cases = int(x.readline())
    players = []
    score = []
    for i in range(cases):
        arr = x.readline().split(":")
        players.append(arr[0])
        score.append(average(arr[1]))
    for i in range(cases):
        print(players[i]+"="+str(score[i]))


               
            
        
