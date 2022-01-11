def gradeCal(a,b):
    c = a*b
    return c
    

uni = []
sub_cnt = int(input('총 과목 개수를 입력해주세요 : '))
# 과목 개수만큼 리스트 안 리스트 생성
for i in range(sub_cnt):
    uni.append([])
while True:
    for i in range(sub_cnt):
        subject = input('과목을 입력해주세요 : ')
        grade = input('등급을 입력해주세요 (ex A+): ')
        credit = int(input('학점을 입력해주세요 (ex 3): '))
    yesno = input('다시 입력하시겠습니까? 네/아니오 : ')
    if yesno == '네':
        for i in range(sub_cnt):
            uni.append([])
        continue
    for i in range(sub_cnt):
        uni[i].append(subject)
        uni[i].append(grade)
        uni[i].append(credit)
    if yesno == '아니오':
        break

grade_tot = 0
for i in range(sub_cnt):
    if uni[i][1] == 'A+' or uni[i][1] == 'a+':
        grade_tot += (4.5*uni[i][2])
    elif uni[i][1] == 'A' or uni[i][1] == 'a':
        grade_tot += (4*uni[i][2])
    elif uni[i][1] == 'B+' or uni[i][1] == 'b+':
        grade_tot += (3.5*uni[i][2])
    elif uni[i][1] == 'B' or uni[i][1] == 'b':
        grade_tot += (3*uni[i][2])
    elif uni[i][1] == 'C+' or uni[i][1] == 'c+':
        grade_tot += (2.5*uni[i][2])
    elif uni[i][1] == 'C' or uni[i][1] == 'c':
        grade_tot += (2*uni[i][2])
    elif uni[i][1] == 'D+' or uni[i][1] == 'd+':
        grade_tot += (1.5*uni[i][2])
    elif uni[i][1] == 'D' or uni[i][1] == 'd':
        grade_tot += uni[i][2]

credit_tot = 0
for i in range(sub_cnt):
    credit_tot += uni[i][2]

avg = grade_tot/credit_tot

for i in range(sub_cnt):
    print(f'과목명 : {uni[i][0]} 등급 : {uni[i][1]} 학점 : {uni[i][2]}')

print(f'최종학점 : {round(avg,2)}')
