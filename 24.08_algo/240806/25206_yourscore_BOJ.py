totalscore = 0
totalgrade = 0
for _ in range(20):
    subject, score, grade = input().split()
    gradenum = 0
    if grade == 'P':
        continue
    elif grade == 'A+':
        gradenum = 4.5
    elif grade == 'A0':
        gradenum = 4.0
    elif grade == 'B+':
        gradenum = 3.5
    elif grade == 'B0':
        gradenum = 3.0
    elif grade == 'C+':
        gradenum = 2.5
    elif grade == 'C0':
        gradenum = 2.0
    elif grade == 'D+':
        gradenum = 1.5
    elif grade == 'D0':
        gradenum = 1.0
    elif grade == 'F':
        gradenum = 0.0
    score = float(score)
    totalscore += score
    totalgrade += gradenum * score
answer = totalgrade/totalscore
print(f'{answer:.6f}')
