#-*- coding:utf-8 -*-

'''
키오스크 처럼 한 번 만들어봤습니다.
일단 사용자들은 처음 화면에서만 선택하면 되고
가게 관리인 같은 경우에는 맨 처음 화면에서 admin을 입력해 관리자 메뉴로 들어갈 수 있습니다.
초기 id는 admin, pw는 admin입니다.
추가 주문 3회 제한하는 것은 그렇게 만들 수는 있지만, 사용자의 불편이 예상돼 제외했습니다.
'''


import kiosk_module

# 집 앞에 미엔이라는 중국집이 있어서 그냥 miyen으로 설정
miyen = kiosk_module.Restaurant()

while True:
    menu_num = input('''1. 메뉴 선택하기
2. 장바구니 보기
3. 장바구니 취소하기
4. 최종 주문하기
번호 입력 : ''')
    print()
    # 사장님 메뉴 들어가기
    if menu_num == 'admin':
        print('사장님 메뉴입니다. 로그인 해주세요.\n')
        if miyen.login():
            while True:
                owner_menu_num = input('''사장님 메뉴입니다.
1. 메뉴 추가하기
2. 메뉴 삭제하기
3. 매출 확인하기
4. id 변경하기
5. pw 변경하기
6. 메인 메뉴로 돌아가기
번호 입력 : ''')
                print()
                # 신메뉴 추가
                if owner_menu_num == '1':
                    miyen.append_menu()
                
                # 메뉴 삭제
                elif owner_menu_num == '2':
                    miyen.delete_menu()
                
                # 매출 확인하기
                elif owner_menu_num == '3':
                    miyen.show_sales()
                
                # id 변경하기
                elif owner_menu_num == '4':
                    miyen.change_id()
                
                # pw 변경하기
                elif owner_menu_num == '5':
                    miyen.change_pw()
                
                # 뒤로가기
                elif owner_menu_num == '6':
                    print('메인 화면으로 돌아갑니다.\n')
                    break
                
                else:
                    print('1,2,3,4,5,6 중 하나를 입력해주세요.\n')
                    
    # 메뉴 선택하기   
    elif menu_num == '1':
        miyen.choose_menu()
        
    # 장바구니 보여주기
    elif menu_num == '2':
        miyen.show_cart()
        
    # 장바구니 삭제하기
    elif menu_num == '3':
        miyen.delete_cart()
    
    # 최종 주문하기
    elif menu_num == '4':
        miyen.pay()
        
    else:
        print('1,2,3,4 중 하나를 입력해주세요.\n')