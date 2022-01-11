import time
import calendar

# 현재 모듈은 포장주문만 받는 가게에서만 사용가능
# 매장 주문도 받는 가게에서 쓸 수 있게 업데이트 필요

class Restaurant:
    def __init__(self):
        self.menu = ['', '짜장면', '삼선간짜장', '해물짬뽕', '삼선짬뽕', '쟁반짜장', '쟁반짬뽕', '짜장밥', '짬뽕밥', '볶음밥', '탕수육 소', '탕수육 중', '탕수육 대']
        self.price = ['', 6500, 8000, 8000, 10000, 19000, 20000, 7000, 8000, 7000, 20000, 25000, 33000]
        self.id = 'admin'
        self.pw = 'admin'
        self.cart = [] # 메뉴이름, 개수, 총 가격 순서
    
    
    
    
    # 메뉴판 보여주기 메소드
    def show_menu(self):
        for i in range(len(self.menu)):
            if i == 0:
                continue
            print('{:2} - {}\t\t{}원'.format(i,self.menu[i],self.price[i]))
        print()
    
    
    
    
    # 장바구니 보여주기 메소드
    def show_cart(self):
        tot_price = 0

        if len(self.cart) == 0:
            print('장바구니에 담긴 품목이 없습니다.\n')

        else:
            for i in range(len(self.cart)):
                print(f'{i+1}\t메뉴명 - {self.cart[i][0]}\t\t주문 개수 - {self.cart[i][1]}개\t\t총 가격 - {self.cart[i][2]}원')
                tot_price += self.cart[i][2]
            print(f'최종가격 - {tot_price}원')
            print()
    
    
    
    
    
    # 장바구니 취소하기 메소드
    def delete_cart(self):
        self.show_cart()
        while True:
            if len(self.cart) == 0:
                print('삭제할 장바구니 품목이 없습니다.')
                break
            while True:
                try:
                    num = int(input('몇 번째 장바구니 품목을 삭제하시겠습니까?\n번호 입력 : ')) - 1  # 인덱스는 0부터 시작이어서
                    print()
                    if num < 0 or num >= len(self.cart):
                        print('해당하는 장바구니 번호가 없습니다.\n')
                        continue
                    break
                except ValueError:
                    print()
                    print('정수를 입력해주세요.\n')
                    continue
                except Exception:
                    print()
                    print('알 수 없는 오류가 발생했습니다.\n')
                    continue
                
            while True:
                yesno = input('정말 삭제하시겠습니까? (y/n)\ny/n 입력 : ')
                print()
                if yesno in ['Y','y','N','n']:
                    break
                else:
                    print('잘못 입력하셨습니다.\n')
                    
            if yesno in ['Y','y']:
                print(f'{num+1}번 장바구니 품목을 삭제합니다.\n')
                del self.cart[num]
                print('삭제 완료, 초기 화면으로 돌아갑니다.\n')
                break
            
            if yesno in ['N','n']:
                print('초기 화면으로 돌아갑니다.\n')
                break
                
        
    
    
    
    
    # 최종 결제 메소드
    def pay(self):
        self.show_cart()
        while True:
            yesno = input('최종 주문하시겠습니까? (y/n)\ny/n 입력 : ')
            print()
            if yesno in ['y','Y','n','N']:
                if yesno in ['y','Y']:
                    now = time.localtime()
                    f = open(f'./sales/{now.tm_year}{str(now.tm_mon).zfill(2)}{str(now.tm_mday).zfill(2)}.txt','a')
                    odr_time = f'{now.tm_hour}:{now.tm_min}:{now.tm_sec}\n'
                    f.write(odr_time)
                    for i in range(len(self.cart)):
                        final = f'메뉴명 - {self.cart[i][0]}\t\t주문 개수 - {self.cart[i][1]}개\t\t총 가격 - {self.cart[i][2]}원\n'
                        f.write(final)
                    f.close()
                    self.cart = []
                    print('주문이 접수 되었습니다.\n')
                    break
                if yesno in ['n','N']:
                    print('메뉴 결정 후 다시 시도해주세요.\n')
                    break
            else:
                print('잘못 입력하셨습니다.\n')
        
        
    
    
    
    
    # 메뉴 선택 메소드
    def choose_menu(self):
        while True:
            self.show_menu()
            while True:
                try:
                    num_choice = int(input('주문하실 메뉴의 번호를 입력해주세요(초기메뉴로 가고싶다면 0을 입력해주세요.)\n메뉴 번호 입력 : '))
                    print()
                    if num_choice < 0 or num_choice >= len(self.menu):
                        print('해당 메뉴 번호가 없습니다.\n')
                        continue
                    break
                except ValueError:
                    print()
                    print('정수를 입력해주세요.\n')
                except Exception:
                    print()
                    print('알 수 없는 오류가 발생했습니다.\n')
            
            if num_choice == 0:
                print('초기 메뉴로 돌아갑니다.\n')
                break

            # 메뉴 개수 입력
            while True:
                try:
                    cnt = int(input('주문 개수를 입력해주세요\n개수 입력 : '))
                    print()
                    if cnt < 1:
                        print('1개 이상 주문해주세요!\n')
                        continue
                    break
                except ValueError:
                    print()
                    print('정수를 입력해주세요\n')
                except Exception:
                    print()
                    print('알 수 없는 오류가 발생했습니다\n.')

            # 장바구니에 넣을건지 다시 한 번 확인
            while True:
                yesno = input('{:2} - {}\t{}개\t총 {}원 장바구니에 넣으시겠습니까? (y/n)\ny/n 입력 : '.format(num_choice, self.menu[num_choice], cnt, self.price[num_choice]*cnt))
                print()
                if yesno in ['y','Y','n','N']:
                    if yesno in ['y','Y']:
                        self.cart.append([self.menu[num_choice], cnt, self.price[num_choice]*cnt])
                        break
                    if yesno in ['n','N']:
                        print('취소합니다.')
                        break
                else:
                    print('잘못 입력하셨습니다.\n')
            
            # 추가주문 의사 확인
            while True:
                addi_yesno = input('이어서 주문하시겠습니까?(y/n)\ny/n 입력 : ')
                print()
                if addi_yesno in ['y','Y','n','N']:
                    if addi_yesno in ['n','N']:
                        print('초기화면으로 돌아갑니다 최종 주문은 4번 메뉴에서 진행해주세요.\n')
                        break
                    else:
                        break
                else:
                    print('잘못 입력하셨습니다.\n')
            
            if addi_yesno in ['n','N']:
                break
                        
                        
                        
################################################# 사장님 메소드 시작 #################################################
    # 로그인 메소드
    def login(self):
        print('id/pw를 틀리면 뒤로 돌아갑니다.')
        owner_id = ''
        owner_pw = ''
        owner_id = input('id : ')
        owner_pw = input('pw : ')
        print()
        if owner_id == self.id and owner_pw == self.pw:
            return True
        else:
            print('id/pw가 틀렸습니다. \n')
            return False
            



    # 메뉴 추가 메소드
    def append_menu(self):
        while True:
            # 추가하려는 메뉴 번호 입력
            while True:
                try:
                    num = int(input('새로 추가하는 메뉴의 번호를 입력해주세요\n(중간 번호를 입력하면 뒤 메뉴들은 한 칸씩 밀리게 됩니다.)\n번호 입력 : '))
                    print()
                    if num < 1:
                        print('1 미만의 숫자는 사용하실 수 없습니다.\n')
                        continue
                    if num > len(self.menu):
                        print('메뉴 번호는 건너뛸 수 없습니다.\n')
                        continue
                    break
                except ValueError:
                    print()
                    print('정수를 입력해주세요.\n')
                except Exception:
                    print()
                    print('알 수 없는 오류가 발생했습니다.\n')

            # 추가하려는 메뉴 이름 입력
            new_menu = input('새로 추가하는 메뉴의 이름을 입력해주세요\n입력 : ')
            print()

            # 추가하려는 메뉴 가격 입력
            while True:
                try:
                    new_price = int(input('새로 추가하는 메뉴의 가격을 입력해주세요\n가격 입력 : '))
                    print()
                    if new_price < 1:
                        print('1 미만의 숫자는 사용하실 수 없습니다.\n')
                        continue
                    break
                except ValueError:
                    print()
                    print('정수를 입력해주세요.\n')
                except Exception:
                    print()
                    print('알 수 없는 오류가 발생했습니다.\n')
                    
            # 입력한 내용이 맞는지 다시 한 번 확인하기
            while True:
                print('입력한 내용이 맞는지 확인해주세요.\n{:2} - {}\t\t{}원'.format(num,new_menu,new_price))
                yesno = input('입력한 내용이 맞다면 y, 아니라면 n을 입력해주세요\ny/n 입력 : ')
                print()
                if yesno not in ['y','Y','n','N']:
                    print('잘못 입력하셨습니다. y/n 중에 입력해주세요.\n')
                    continue
                if yesno in ['y','Y']:
                    break
                if yesno in ['n','N']:
                    print('메뉴 추가 화면 처음으로 돌아갑니다.')
                    break
            
            # 사용자가 맞게 입력했다고 할 때 리스트에 추가 및 반복문 종료
            if yesno in ['y', 'Y']:
                self.menu.insert(num,new_menu)
                self.price.insert(num,new_price)
                print('{} - {}\t\t{}원  추가했습니다.\n'.format(num,self.menu[num],self.price[num]))
                break
    
    # 메뉴 삭제하기 메소드
    def delete_menu(self):
        if len(self.menu) == 1:
            print('삭제할 메뉴가 없습니다.\n')
        else:
            while True:
                self.show_menu()
                while True:
                    try:
                        delete_num = int(input('삭제할 메뉴의 번호를 입력해주세요.\n번호 입력 : '))
                        print()
                        if delete_num < 1:
                            print('1 미만의 숫자는 사용하실 수 없습니다.\n')
                            continue
                        elif delete_num >= len(self.menu):
                            print('해당하는 메뉴 번호가 존재하지 않습니다.\n')
                            continue
                        break
                    except ValueError:
                        print()
                        print('정수를 입력해주세요.\n')
                    except Exception:
                        print()
                        print('알 수 없는 오류가 발생했습니다.\n')

                while True:
                    yesno = input('{:2} - {}\t\t{} 삭제하시겠습니까?\n맞다면 y, 아니라면 n을 입력해주세요\ny/n 입력 : '.format(delete_num,self.menu[delete_num],self.price[delete_num]))
                    print()
                    if yesno not in ['y', 'Y', 'n', 'N']:
                        print('잘못 입력하셨습니다.\n')
                    else:
                        break
                    
                if yesno in ['y', 'Y']:
                    print('{:2} - {}\t\t{} 삭제합니다.\n'.format(delete_num,self.menu[delete_num],self.price[delete_num]))
                    del self.menu[delete_num]
                    del self.price[delete_num]
                    print('삭제 완료, 이전 화면으로 돌아갑니다.\n')
                    break
                
                elif yesno in ['n', 'N']:
                    print('이전 화면으로 돌아갑니다.\n')
                    break
                
    # 매출 확인하기 메소드
    def show_sales(self):
        print('확인하고자 하는 날짜를 입력해 주세요\n')
        now = time.localtime()
        print(calendar.calendar(now.tm_year))
        print()
        while True:
            try:
                year = int(input('year : '))
                month = int(input('month : '))
                day = int(input('day : '))
                print()
                if year < 1 or month < 1 or day < 1:
                    print('0 이하의 숫자는 사용할 수 없습니다.\n')
                    continue
                if year < 1900:
                    print('1900년 이후로 입력해주세요.')
                    continue
                if month > 12:
                    print('12월이 최대입니다.\n')
                    continue
                if day > 31:
                    print('31일이 최대입니다.\n')
                    continue
                break
            except ValueError:
                print()
                print('정수를 입력해주세요.\n')
            except Exception:
                print()
                print('알 수 없는 오류가 발생했습니다.\n')
                
        try:
            print(f'{year}년 {month}월 {day}일 매출을 조회합니다.\n')
            date = str(year)+str(month).zfill(2)+str(day).zfill(2)
            f = open(f'./sales/{date}.txt','r')
            while True:
                line = f.readline()
                if not line:
                    break
                print(line.strip('\n'))
            f.close()
            print()
        except FileNotFoundError:
            print('해당하는 날짜의 매출이 존재하지 않습니다.\n')
        except Exception:
            print('알 수 없는 에러가 발생했습니다.\n')
            
            
    # id 변경 메소드
    def change_id(self):
        print('id를 변경하려면 로그인해주세요.')
        self.login()
        while True:
            new_id = input('새로운 id를 입력해주세요(5글자 이상)\n새 id 입력 : ')
            print()
            if len(new_id) < 5:
                print('5글자 이상 입력해주세요.\n')
                continue
            new_id_again = input('새로운 id를 다시 한 번 입력해주세요(5글자 이상)\n새 id 입력 : ')
            print()
            if new_id == new_id_again:
                while True:
                    yesno = input('정말로 id를 변경하시겠습니까?(y/n)\ny/n 입력 : ')
                    print()
                    if yesno in ['Y','y','N','n']:
                        break
                    else:
                        print('잘못 입력하셨습니다.\n')
                        continue
                break
            else:
                print('일치하지 않습니다.\n')
                continue
                
        if yesno in ['Y','y']:
            print('id를 변경합니다.\n')
            self.id = new_id
            print('id 변경 완료.\n')
            
        if yesno in ['N','n']:
            print('변경되지 않았습니다.\n')
            
            
    # pw 변경 메소드
    def change_pw(self):
        print('pw를 변경하려면 로그인해주세요.')
        self.login()
        while True:
            new_pw = input('새로운 pw를 입력해주세요(5글자 이상)\n새 pw 입력 : ')
            print()
            if len(new_pw) < 5:
                print('5글자 이상 입력해주세요.\n')
                continue
            new_pw_again = input('새로운 pw를 다시 한 번 입력해주세요(5글자 이상)\n새 pw 입력 : ')
            print()
            if new_pw == new_pw_again:
                while True:
                    yesno = input('정말로 pw를 변경하시겠습니까?(y/n)\ny/n 입력 : ')
                    print()
                    if yesno in ['Y','y','N','n']:
                        break
                    else:
                        print('잘못 입력하셨습니다.\n')
                        continue
                break
            else:
                print('일치하지 않습니다.\n')
                continue
                
        if yesno in ['Y','y']:
            print('pw를 변경합니다.\n')
            self.pw = new_pw
            print('pw 변경 완료.\n')
            
        if yesno in ['N','n']:
            print('변경되지 않았습니다.\n')