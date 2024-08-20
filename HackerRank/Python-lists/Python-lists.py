if __name__ == '__main__':
    
    #N is how we read in the number of commands
    #to take as input
    N = int(input())

    #list of commands
    myArr = []
    
    #Take the inputs N number of times and
    #put them in the list named myArr
    for x in range(N):
        
        #Split the input into a string
        #Remember that a string is also an array
        temp = input().split()
        
        #Perform the following commands
        if(temp[0] == "insert"):
            myArr.insert(int(temp[1]), int(temp[2]))
        elif(temp[0] == "print"):
            print(myArr)
        elif(temp[0] == "remove"):
            myArr.remove(int(temp[1]))
        elif(temp[0] == "append"):
            myArr.append(int(temp[1]))
        elif(temp[0] == "sort"):
            myArr.sort()
        elif(temp[0] == "pop"):
            myArr.pop()
        elif(temp[0] == "reverse"):
            myArr.reverse()
        