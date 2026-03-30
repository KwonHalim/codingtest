from collections import Counter

def solution(citations):
    answer = 0
    idx = 0
    citations.sort(reverse = True)
    print(citations)
    for i in citations:
        idx+=1
        if idx <= i:
            answer = idx
    return answer