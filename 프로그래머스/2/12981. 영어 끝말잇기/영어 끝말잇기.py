from math import floor

def solution(n, words):
    answer = []
    
# 0,1,2, 3,4,5, 6,7,8 -> 3,3
# 0,1 2,3 4,5 6,7
    
    record = set()
    record.add(words[0])
    for i in range(1,len(words)):
        # print(words[i][-1], words[i+1][0])
        if (words[i][0] != words[i-1][-1]) or (words[i] in record):
            print(words[i])
            return [i%n+1,floor(i/n)+1]
        else:
            record.add(words[i])
        # print(words[i])
        
        

    return [0,0]