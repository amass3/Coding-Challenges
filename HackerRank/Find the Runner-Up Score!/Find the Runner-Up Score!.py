if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    
    #In Python 3, map returns an iterable object of type map, 
    #and not a subscriptible list, which would allow you 
    #to write map[i]. To force a list result, write
    # Example: payIntList = list(map(int,payList))
    myList = list(arr)
    
    #Store the first maximum number from myList
    firstMax = max(myList)
   
    #Remove all first maximum numbers from myList
    for i in range(n):
        if firstMax in myList:
            myList.remove(firstMax)
            #Decrement n because myList length changes with every removal
            n -= 1
    
    #Store the new maximum number         
    secondMax = max(myList)
    
    print(secondMax)
