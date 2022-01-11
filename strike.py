# 랜덤 모듈 가져오기
import random

# 난수 발생시키기 
while True:
    hund = str(random.randrange(0,10))
    ten = str(random.randrange(0,10))
    one = str(random.randrange(0,10))
    if hund == ten :
        continue
    elif hund == one :
        continue
    elif ten == one : 
        continue
    com = hund + ten + one
    break

count = 0

while True:
    strike = 0
    ball = 0
    player = input('숫자를 입력해주세요 : ')
    print()
    for i in range(3):
        for j in range(3):
            if player[i] == com[i]:
                strike += 1
            elif player[i] == com[j] and i != j:
                ball += 1
    count += 1
    print(f'{strike} 스트라이크!')
    print(f'{ball} 볼!')
    print(f'도전 횟수 : {count}')
    print()
    if strike == 3:
        print('맞췄습니다.\n')
        while True:
            yesno = input('다시 하시겠습니까?\n네 / 아니오 : ')
            print()
            if yesno == '네':
                count = 0
                while True:
                    hund = str(random.randrange(0,10))
                    ten = str(random.randrange(0,10))
                    one = str(random.randrange(0,10))
                    if hund == ten :
                        continue
                    elif hund == one :
                        continue
                    elif ten == one : 
                        continue
                    com = hund + ten + one
                    break
                break
            elif yesno == '아니오':
                break
            else:
                print('잘못 입력하셨습니다.\n')
        if yesno == '아니오':
            print('종료합니다.')
            break