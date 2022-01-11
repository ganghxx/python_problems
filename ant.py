# 개미수열

def ant(num, cnt):
    '''첫번째 요소로 시작할 숫자를, 두번째는 반복횟수를 넣어주세요'''
    print(num)
    print()
    if cnt == 1:
        return num
    # 정수형으로 변환해 맞는 타입인지 확인
    num, cnt = int(num), int(cnt)
    # 문자열로 변환(iterable객체로 사용하기 위해)
    num = str(num)
    new = ''
    temp = []
    for i in range(len(num)):
        try:
            next_num = num[i+1]
        except IndexError:
            temp.append(num[i])
            new += temp[0]
            new += str(len(temp))
        else:
            if num[i] == next_num:
                temp.append(num[i])
            else:
                temp.append(num[i])
                new += temp[0]
                new += str(len(temp))
                temp = []
    new = int(new)
    return ant(new, cnt-1)

ant(1,5)