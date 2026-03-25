def solution(n):
    answer = 0
    l = str(bin(n)).count("1")
    while True:
        n+=1
        cnt = str(bin(n)).count("1")
        if cnt == l:
            return n
    
# 1001110
# 1010011
# 1010110
# 1011100
# 1100011



# 1111
# 10111
    return answer