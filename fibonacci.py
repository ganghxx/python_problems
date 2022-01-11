# 피보나치 수열

def fibonacci(cnt, num_list=[1,1]):
    print(num_list)
    if cnt == 0:
        return num_list
    num_list.append(num_list[-1] + num_list[-2])
    return fibonacci(cnt-1, num_list)
    
fibonacci(10)