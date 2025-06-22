'''
1번: 1,2,3,4,5 반복
2번: 2,1,2,2,2,3,2,4,2,5 반복
3번: 3,3,1,1,2,2,4,4,5,5 반복
'''

def solution(answers):
    one_score = 0
    two_score = 0
    three_score = 0
    one = [1,2,3,4,5]
    two = [2,1,2,3,2,4,2,5]
    three = [3,3,1,1,2,2,4,4,5,5]
    answer = []

    for i in range(len(answers)):
        if(one[i%5] == answers[i]):
            one_score+=1
        if(two[i%8] == answers[i]):
            two_score+=1
        if(three[i%10] == answers[i]):
            three_score+=1
    highest = max(one_score, two_score, three_score)
    if(one_score == highest):
        answer.append(1)
    if(two_score == highest):
        answer.append(2)
    if(three_score == highest):
        answer.append(3)
    answer.sort()
    return answer