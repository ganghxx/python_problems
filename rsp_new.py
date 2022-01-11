# 컴퓨터가 랜덤한 결과를 가져오게 모듈 호출
import random

rsp = {-1:'end', 0:'가위', 1:'바위', 2:'보'}

# 사용자와 컴퓨터의 선택지로 승(1),무(0),패(-1)를 반환하는 함수
def winlose_output(player, com):
    if player == '가위':
        if com == '가위':
            return 0
        if com == '바위':
            return -1
        if com == '보':
            return 1
    if player == '바위':
        if com == '가위':
            return 1
        if com == '바위':
            return 0
        if com == '보':
            return -1
    if player == '보':
        if com == '가위':
            return -1
        if com == '바위':
            return 1
        if com == '보':
            return 0

# 사용자의 입력값을 받아오는 함수
def player_input():
    try:
        player = int(input('가위바위보! (가위 : 0, 바위 : 1, 보 : 2, 종료 : -1) >>>'))
        print()
    except ValueError:
        print('정수만 입력 가능합니다.')
        print()
        return player_input()
    else:
        if player < -1 or player > 2:
            print('-1~2의 값만 입력해주세요.')
            print()
            return player_input()
        else:
            return player

# 실행하는 코드
win_count = 0
while True:
    com = rsp[random.randint(0,2)]
    player = rsp[player_input()]
    if player == 'end':
        print(f'종료합니다. 최종점수 : {win_count}')
        break
    else:
        winlose = winlose_output(player, com)
        print('player : {:2}, com : {:2}'.format(player, com))
        if winlose == 1:
            win_count += 1
            print(f'이겼습니다!\t승점 : {win_count}')
        if winlose == 0:
            print(f'비겼습니다.\t승점 : {win_count}')
        if winlose == -1:
            win_count -= 1
            print(f'졌습니다ㅠㅠ\t승점 : {win_count}')
        print()