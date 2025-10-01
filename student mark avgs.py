#The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. Print the average of the marks array for the student name provided, showing 2 places after the decimal.
if __name__ == '__main__':
    n = int(input()) #number of students records
    student_marks = {}
    for _ in range(n): # names and marks obtained by students
        name, *line = input().split() # key = name : value pairs = marks array for each
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    # print(student_marks.get(query_name))
    average = sum(student_marks.get(query_name)) / len(student_marks.get(query_name))
    print(f"{average:.2f}") # prints exactly 2 trailing decimal places
    
