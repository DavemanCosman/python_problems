# Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

#Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.
if __name__ == '__main__':
    records =[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name,score])
    
    records.sort()
    unique_scores = sorted(list(
        {score[1] for score in records}
    ),reverse=False)
    
    #print(unique_scores)
    second_lowest = unique_scores[1] # 2nd unique score will be 2nd lowest score
    
    for record in range(len(records)):
        if records[record][1] == second_lowest:
            print(records[record][0])
            
            
# 5
# Harsh
# 20
# Beria
# 20
# Varun
# 19
# Kakunami
# 19
# Vikas
# 21