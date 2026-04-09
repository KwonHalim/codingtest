from math import gcd

def solution(arr):
    answer = 0
    tmp = arr[0]
    for i in arr:
        LCM = tmp*i // gcd(tmp,i)
        tmp = LCM
        
    return LCM