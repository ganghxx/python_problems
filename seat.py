# 초기 세팅
# 좌석 설정
# 에디터 재시작시 다시 실행
seat = []
how_many_seats = 101 # 좌석 개수 설정 (원하는 개수 + 1 적기)
for i in range(1,how_many_seats): # 좌석 개수 재설정시, 에디터 재실행시 리스트 새로 생성
    seat.append([i])

# 입실 함수 생성
def entrance(num,name):
    seat[num-1].append(name)

# 퇴실 함수 생성
def exit(num):
    seat[num-1].pop()

#시간 모듈 가져오기
import time

# 반복문 시작
while True:
    menu = input('''
원하시는 메뉴의 숫자를 입력해주세요. 
1) 입실
2) 퇴실
3) 좌석 현황 보기
4) 사용자 자리 찾기
5) 빈 자리 찾기
6) 전원 퇴실(좌석 초기화)
7) 시스템 종료
입력 : ''')
    # 입실을 선택했을 때
    if menu == '1':
        print('\n입실을 선택하셨습니다.\n사용자 이름과 원하시는 좌석을 입력해주세요.')
        while True:
            # 입실 사용자 이름 입력
            name = input('사용자 이름 : ') 
            # 입실 희망 좌석 번호 입력
            num = int(input('원하시는 좌석 번호 : ')) 
            print()
            # 리스트 인덱스 번호가 실제 좌석 번호보다 1 작음 real_num = 실제 리스트 인덱스
            real_num = num-1

            # 존재하는 좌석 번호 외 값을 입력했을 때
            if num < 1 or num > how_many_seats-1:
                print('\n잘못 입력하셨습니다. 다시 시도해 주세요.')
            # 희망 좌석에 이미 입실 인원이 있을 때
            elif len(seat[real_num]) == 2: 
                print('\n이미 사용 중인 좌석입니다.')
                break
            # 희망 좌석에 입실 가능할 때
            elif len(seat[real_num]) == 1: 
                entrance(num,name)
                print('입실하셨습니다.\n사용자 이름 : ' + seat[real_num][1] + f'\n선택한 좌석 : {num}번')
                now = time.localtime()
                print('입실 시간 : ' + f'{now.tm_year}/{now.tm_mon}/{now.tm_mday} {now.tm_hour}:{now.tm_min}:{now.tm_sec}')
                break
            
    # 퇴실을 선택했을 때
    elif menu == '2':
        print('\n퇴실을 선택하셨습니다.\n퇴실하시는 좌석의 번호를 입력해주세요.')
        while True:
            # 퇴실 희망 번호 입력
            num = int(input('퇴실하시는 좌석 번호 : ')) 
            print()
            # 리스트 인덱스 번호가 실제 좌석 번호보다 1 작음 real_num = 실제 리스트 인덱스
            real_num = num-1 

            # 존재하는 좌석 번호 외 값을 입력했을 때
            if num < 1 or num > how_many_seats-1:
                print('\n잘못 입력하셨습니다. 다시 시도해 주세요.')
            # 퇴실 절차 실행
            elif len(seat[real_num]) == 2:
                # 퇴실 더블 체크
                while True:
                    make_sure = input(f'\n{seat[real_num][1]}님 정말 퇴실하시겠습니까?\n네 / 아니오 : ') 
                    if make_sure == "네":
                        print('\n퇴실하셨습니다.\n사용자 이름 : ' + seat[real_num][1] + f'\n퇴실하시는 좌석 : {num}번')
                        now = time.localtime()
                        print('퇴실 시간 : ' + f'{now.tm_year}/{now.tm_mon}/{now.tm_mday} {now.tm_hour}:{now.tm_min}:{now.tm_sec}')
                        exit(num)
                        break
                    elif make_sure == '아니오':
                        print('\n메인 메뉴로 돌아갑니다.')
                        break
                    # 네 / 아니오 중 입력하지 않았을 때
                    else:
                        print('\n잘못 입력하셨습니다. 다시 시도해주세요.')
                break
            # 아직 입실하지 않은 좌석을 퇴실할 때
            elif len(seat[real_num]) == 1:
                print(f'\n{num}번 좌석에는 아직 입실하지 않았습니다.')
                break
            
    # 좌석 현황 보기를 선택했을 때
    elif menu == '3':
        print('-'*40 + '좌석 현황' + '-'*40)
        for i in range(0,how_many_seats-1):
            if i % 10 ==0:
                    print('\n')
            print(seat[i], end = ' ')
        print('\n\n'+'-'*89)
    
    #사용자 자리 찾기를 선택했을 때
    elif menu == '4':
        print('\n사용자 자리 찾기를 선택하셨습니다.\n찾고싶으신 사용자의 이름을 입력해주세요.')
        # 좌석 위치를 찾을 사용자 이름 입력
        name = input('사용자 이름 입력 : ')
        for i in range(0,how_many_seats-1):
            zari = seat[i][0]
            if len(seat[i]) == 1:
                continue
            else:
                if name != seat[i][1]:
                    print('\n해당하는 인원이 없습니다.')
                else:
                    print(f'\n{name}님은 현재 {zari}번에 입실 중입니다.')
    
    # 빈좌석 찾기를 선택했을 때
    elif menu == '5':
        print('-'*20 + '빈좌석 리스트' + '-'*20)
        for i in range(0,how_many_seats-1):
            if len(seat[i]) == 1:
                if i % 10 ==0:
                    print('\n')
                # zari = 좌석 번호를 받아오기 위한 식별자
                zari = seat[i][0]
                print(f'{zari}번', end = ' ')
        print('\n\n'+'-'*53)
        print()

    # 전원 퇴실(좌석 초기화)
    elif menu == '6':
        # 리스트에서 값을 빼기보단 그냥 리스트 다시 만듦
        while True:
        # 전원 퇴실 더블 체크
            make_sure = input('\n 전원 퇴실 처리를 합니다. 정말 하시겠습니까?\n네 / 아니오 : ')
            if make_sure == '네':
                seat = []
                for i in range(1,how_many_seats):
                    seat.append([i])
                print('\n전원 퇴실 처리가 완료됐습니다.')
                break
            elif make_sure == '아니오':
                print('\n메인메뉴로 돌아갑니다.')
                break
            # 네 / 아니오 중 입력하지 않았을 때
            else:
                print('\n잘못 입력하셨습니다. 다시 시도해주세요.')

    # 시스템 종료
    elif menu == '7':
        # 시스템 종료 더블 체크
        while True:
            make_sure = input('\n시스템을 종료합니다.정말 종료하시겠습니까?\n네 / 아니오 : ')
            if make_sure == '네':
                print('\n시스템을 종료합니다.')
                break
            elif make_sure == '아니오':
                print('\n메인메뉴로 돌아갑니다.')
                break
            # 네 / 아니오 중 입력하지 않았을 때
            else:
                print('\n잘못 입력하셨습니다. 다시 시도해주세요.')
        if make_sure == '네':
            break
    
    # menu에서 1~7 외 다른 정수를 입력했을 때
    else:
        print('\n잘못 입력하셨습니다.')