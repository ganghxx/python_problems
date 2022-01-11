# 영어는 영어대로 정렬 후 숫자는 모두 더한 후 뒤에 적기

text = "AJKDLSI412K4JSJ9D"
result = ''
temp = ''
hap = 0
for i in text:
    try:
        i = int(i)
    except ValueError:
        temp += i
    else:
        hap += i

temp = "".join(sorted(temp))

result = temp + str(hap)

print(result)