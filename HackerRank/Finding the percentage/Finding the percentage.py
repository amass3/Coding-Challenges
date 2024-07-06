if __name__ == '__main__':
    
    #The number of students in the dictionary
    n = int(input())
    
    #The dictionary of the list of students
    student_marks = {}
    
    #constructing a dictionary of a list of students
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    
    #The student name provided
    query_name = input()
    
    #The total number of values and the average
    total = 0
    average = 0
    
    #Calculate the total of the query_name
    for x in student_marks[query_name]:
        total += x 
    
    #Calculate the average and print it
    average = total/3
    
    print(format((average), ".2f"))
