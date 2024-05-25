import math

if __name__ == '__main__':
    
    #Nested list of names and scores
    myList = []
    
    #List of scores
    listOfScores = []
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        #Create the nested list and store names and scores
        myList.append([name,score])
    
    #Retrieve the scores and store them in a list
    for i in range(len(myList)):
        listOfScores.append(myList[i][1])
    
    
    #Find the second lowest score
    low1, low2 = math.inf, math.inf
        
    #Fisrt Lowest score
    for x in range(len(listOfScores)):
        if listOfScores[x] < low1:
            low1 = listOfScores[x]
            
    #Second Lowest Score
    for k in range(len(listOfScores)):
        if listOfScores[k] != low1 and listOfScores[k] < low2:
            low2 = listOfScores[k]
    
    #The list of names with the lowest score
    namesWithLowScores = []
    
    #Get the names of the students with the lowest scores
    for i in range(len(myList)):
        if myList[i][1] == low2:
            namesWithLowScores.append(myList[i][0])
    
    #Sort the names in alphabetic order
    namesWithLowScores.sort()
    
    #Display result
    for i in range(len(namesWithLowScores)):
        print(namesWithLowScores[i])
