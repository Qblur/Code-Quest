with open('Prob02.in.txt') as x:
    T = int(x.readline())
    for i in range(0, T):
        z = x.readline()
        y = z.find(' ')+1
        pos = int(z[y:]) #finds the index of the char to be removed
        y = y-1 
        znew = z[:y] #removes the space and the integer at the end
        p = znew[:pos]+znew[pos+1:] #create a new string that removes the integer
        print(p)
                  
        
        
