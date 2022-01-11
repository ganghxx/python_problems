'''
문제 1번: https://tech.kakao.com/2017/09/27/kakao-blind-recruitment-round-1/
'''

n = 6

arr1 = [46,33,33,22,31,50]
arr2 = [27,56,19,14,14,10]

arr1 = list(map(lambda x:bin(x)[2:].zfill(n), arr1))
arr2 = list(map(lambda x:bin(x)[2:].zfill(n), arr2))

result = []
for i in range(n):
    first = arr1[i]
    second = arr2[i]
    temp_txt = ''
    for j in range(n):
        if first[j] == '1' or second[j] =='1':
            temp_txt += '#'
        else:
            temp_txt += ' '
    result.append(temp_txt)
    
print(result)