def solution(bandage, health, attacks):
    j = 0 #attacks횟수용 변수
    hp = health #현재 체력
    k = 0 #연속 치료 성공 여부 확인용
    for i in range(attacks[-1][0] + 1):
        if(i!=attacks[j][0]):
            if(hp < health) and (k == bandage[0]):
                hp = hp + bandage[1] + bandage[2]
                k = 0
                if(hp > health): #초과 체력 초기화
                    hp = health
            elif(hp < health):
                hp = hp + bandage[1]
                k = k + 1
                
                if(k == bandage[0]): #카운트 1일때, 바로 회복 여부
                    hp = hp + bandage[2]
                    k = 0
                
                if(hp > health):#초과 체력 초기화
                    hp = health
                
            else:
                hp = health
        else:
            hp = hp - attacks[j][1]
            j +=1
            k = 0
            if(hp <= 0):
                return -1
        print("현재상태:", hp, "연속성공:", k)
    return hp