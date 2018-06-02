with open("Prob06.in.txt") as x:
    cases = int(x.readline())
    for i in range(0, cases):
        line = x.readline().replace("\n", "")
        line = line.split(" ")
        value = 0
        if line[0] == "BROKEN":
            value += 8
        if line[1] == "BROKEN":
            value += 4
        if line[2] == "BROKEN":
            value += 2
        if line[3] == "BROKEN":
            value += 1
        left = "off"
        right = "off"
        rightval = value % 4
        leftval = value // 4
        if rightval == 1:
            right = "red"
        elif rightval == 2:
            right = "green"
        elif rightval == 3:
            right = "blue"

        if leftval == 1:
            left = "red"
        elif leftval == 2:
            left = "green"
        elif leftval == 3:
            left = "blue"  
        print(left+" "+right)     
        
            
