import random
random = random.randrange(1,101) # 숫자 범위 조정
player = int(input('업? 다운?\n숫자를 입력해 주세요 : '))
while True:
    if player < random:
        player = int(input('업!\n숫자를 입력해 주세요 : '))
    elif player > random:
        player = int(input('다운!\n숫자를 입력해 주세요 : '))
    else:
        print('맞췄습니다!')
        break