# uni = [[과목1, a+, 2]. [과목2, b+, 3]...]
# 주의!!!!
# 아직은 숫자를 입력해야하는 곳에 문자를 입력하면 에러 발생(음수 입력시에만 다시 입력하라고 출력)
# 등급 적는 곳에는 아무거나 넣어도 등급 외에는 다시 입력하라고 출력

def gradeCal(a,b):
    'a = (등급), b = (이수 학점)'
    if a == 'a+':
        return 4.5 * b
    if a == 'a':
        return 4 * b
    if a == 'b+':
        return 3.5 * b
    if a == 'b':
        return 3 * b
    if a == 'c+':
        return 2.5 * b
    if a == 'c':
        return 2 * b
    if a == 'd+':
        return 1.5 * b
    if a == 'd':
        return b

uni = []
grade_tot = 0
credit_tot = 0

while True:
    # 총 과목 개수 입력
    while True:
        sub_cnt = int(input('총 과목 개수를 입력해주세요 : ')) # 총 과목 개수 입력
        print()
        # 음수 값 입력 방지
        if sub_cnt >= 1:
            break
        else:
            print('1 이상의 숫자를 입력해주세요.\n')
            
    # 등급 및 수업 당 학점 입력
    for i in range(sub_cnt):
        uni.append([])
        subject = input('과목을 입력해주세요 : ') # 과목 이름 입력
        uni[i].append(subject)
        
        # 등급 입력
        while True:
            grade = input('등급을 소문자로 입력해주세요 (ex a+): ')
            # 등급 외 값 입력 방지
            # if grade not in 'a+b+c+d+' 를 사용하고 싶었으나, a+b 등의 오탈자가 호오오옥시라도 있을 경우를 대비해 그냥 하나하나 입력
            if grade != 'a+' and  grade != 'a' and grade != 'b+' and grade != 'b' and grade != 'c+' and grade != 'c' and grade != 'd+' and grade != 'd':
                print('\n등급을 잘못 입력하셨습니다.\n')
                continue
            else:
                uni[i].append(grade)
                break
                
        # 학점 입력
        while True:
            credit = int(input('학점을 입력해주세요 (ex 3): '))
            # 학점 음수 방지
            if credit > 0:
                uni[i].append(credit)
                break
            else:
                print('1 이상의 숫자를 입력해주세요.')
        print()
        # 전체 이수 학점 계산
        credit_tot += uni[i][2]
        # 전체 (등급 * 학점) 계산
        grade_tot += gradeCal(uni[i][1],uni[i][2])

    # 다시 입력할 것인지 질문하기
    while True:
        yesno = input('\n처음부터 다시 입력하시겠습니까? 네/아니오 : ')
        print()
        # 네/ 아니오 오입력 방지
        if yesno == '네':
            uni = []
            for i in range(sub_cnt):
                uni.append([])
            break
        if yesno == '아니오':
            break
        else:
            print('잘못 입력하셨습니다.')
    
    if yesno == '아니오':
        break

avg = grade_tot/credit_tot
print()
print('='*50)
for i in range(sub_cnt):
    print(f'과목명 : {uni[i][0]} 등급 : {uni[i][1]} 학점 : {uni[i][2]}')
print(f'최종학점 : {round(avg,2)}')
print('='*50)