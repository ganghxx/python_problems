# 랜덤 모듈 가져오기
import random

# 경우의 수 리스트 생성
rsp = ['가위', '바위', '보']

# 승점
count = 0

while True:
    # 플레이어 선택 입력
    player = input('가위 바위 보!\n플레이어 : ')
    
    #가위를 냈을 때
    if player == '가위':
        cpu_random = random.randrange(0,3)
        # 컴퓨터 가위를 골랐을 때
        if rsp[cpu_random] == '가위':
            print(f'컴퓨터 : {rsp[cpu_random]}')
            print('비겼습니다.')
            print(f'승점 : {count}')
            while True:
                yesno = input('\n다시 하시겠습니까?\n네 / 아니오 : ')
                print()
                if yesno == '네':
                    break
                elif yesno == '아니오':
                    break
                elif yesno != '네' and '아니오':
                    print('잘못 입력하셨습니다.')
                    continue
            if yesno == '아니오':
                print('\n종료합니다.')
                break
                
        # 컴퓨터 바위를 골랐을 때
        elif rsp[cpu_random] == '바위':
            print(f'컴퓨터 : {rsp[cpu_random]}')
            print('졌습니다.')
            count -= 1
            print(f'승점 : {count}')
            while True:
                yesno = input('\n다시 하시겠습니까?\n네 / 아니오 : ')
                print()
                if yesno == '네':
                    break
                elif yesno == '아니오':
                    break
                elif yesno != '네' and '아니오':
                    print('잘못 입력하셨습니다.')
                    continue
            if yesno == '아니오':
                print('\n종료합니다.')
                break
            
        # 컴퓨터 보를 골랐을 때
        elif rsp[cpu_random] == '보':
            print(f'컴퓨터 : {rsp[cpu_random]}')
            print('이겼습니다.')
            count += 1
            print(f'승점 : {count}')
            while True:
                yesno = input('\n다시 하시겠습니까?\n네 / 아니오 : ')
                print()
                if yesno == '네':
                    break
                elif yesno == '아니오':
                    break
                elif yesno != '네' and '아니오':
                    print('잘못 입력하셨습니다.')
                    continue
            if yesno == '아니오':
                print('\n종료합니다.')
                break
            
    # 바위를 냈을 때
    elif player == '바위':
        cpu_random = random.randrange(0,3)
        # 컴퓨터 가위를 골랐을 때
        if rsp[cpu_random] == '가위':
            print(f'컴퓨터 : {rsp[cpu_random]}')
            print('이겼습니다.')
            count += 1
            print(f'승점 : {count}')
            while True:
                yesno = input('\n다시 하시겠습니까?\n네 / 아니오 : ')
                print()
                if yesno == '네':
                    break
                elif yesno == '아니오':
                    break
                elif yesno != '네' and '아니오':
                    print('잘못 입력하셨습니다.')
                    continue
            if yesno == '아니오':
                print('\n종료합니다.')
                break
                
        # 컴퓨터 바위를 골랐을 때
        elif rsp[cpu_random] == '바위':
            print(f'컴퓨터 : {rsp[cpu_random]}')
            print('비겼습니다.')
            print(f'승점 : {count}')
            while True:
                yesno = input('\n다시 하시겠습니까?\n네 / 아니오 : ')
                print()
                if yesno == '네':
                    break
                elif yesno == '아니오':
                    break
                elif yesno != '네' and '아니오':
                    print('잘못 입력하셨습니다.')
                    continue
            if yesno == '아니오':
                print('\n종료합니다.')
                break
            
        # 컴퓨터 보를 골랐을 때
        elif rsp[cpu_random] == '보':
            print(f'컴퓨터 : {rsp[cpu_random]}')
            print('졌습니다.')
            count -= 1
            print(f'승점 : {count}')
            while True:
                yesno = input('\n다시 하시겠습니까?\n네 / 아니오 : ')
                print()
                if yesno == '네':
                    break
                elif yesno == '아니오':
                    break
                elif yesno != '네' and '아니오':
                    print('잘못 입력하셨습니다.')
                    continue
            if yesno == '아니오':
                print('\n종료합니다.')
                break
    
    # 보를 냈을 때
    elif player == '보':
        cpu_random = random.randrange(0,3)
        # 컴퓨터 가위를 골랐을 때
        if rsp[cpu_random] == '가위':
            print(f'컴퓨터 : {rsp[cpu_random]}')
            print('졌습니다.')
            count -= 1
            print(f'승점 : {count}')
            while True:
                yesno = input('\n다시 하시겠습니까?\n네 / 아니오 : ')
                print()
                if yesno == '네':
                    break
                elif yesno == '아니오':
                    break
                elif yesno != '네' and '아니오':
                    print('잘못 입력하셨습니다.')
                    continue
            if yesno == '아니오':
                print('\n종료합니다.')
                break
                
        # 컴퓨터 바위를 골랐을 때
        elif rsp[cpu_random] == '바위':
            print(f'컴퓨터 : {rsp[cpu_random]}')
            print('이겼습니다.')
            count += 1
            print(f'승점 : {count}')
            while True:
                yesno = input('\n다시 하시겠습니까?\n네 / 아니오 : ')
                print()
                if yesno == '네':
                    break
                elif yesno == '아니오':
                    break
                elif yesno != '네' and '아니오':
                    print('잘못 입력하셨습니다.')
                    continue
            if yesno == '아니오':
                print('\n종료합니다.')
                break
            
        # 컴퓨터 보를 골랐을 때
        elif rsp[cpu_random] == '보':
            print(f'컴퓨터 : {rsp[cpu_random]}')
            print('비겼습니다.')
            print(f'승점 : {count}')
            while True:
                yesno = input('\n다시 하시겠습니까?\n네 / 아니오 : ')
                print()
                if yesno == '네':
                    break
                elif yesno == '아니오':
                    break
                elif yesno != '네' and '아니오':
                    print('잘못 입력하셨습니다.')
                    continue
            if yesno == '아니오':
                print('\n종료합니다.')
                break
        
    # 잘못 입력했을 떄
    else:
        print('\n잘못 입력하셨습니다.')