from math import ceil

def solution(fees, records):
    answer = []
    dic = {}
    car_fee = {}
    
    
    for record in records:
        a,car,park = map(str, record.split(" "))
        # print(a,b,c)
        h,m = map(int,a.split(":"))
        time = h*60 + m
        # print(time,car,park)
        
        if park == 'IN':
            dic[car] = time
            
        elif park == 'OUT':
            in_time = dic[car]
            park_time = time - in_time
            if car in car_fee:
                car_fee[car] = car_fee[car] + park_time
            else:
                car_fee[car] = park_time
            del dic[car]
#             입차 기록은 있으나 나가지 12시가 넘어도 나가지 않은 차들
    for car in dic:
        max_time = 23*60+59
        if car in car_fee:
            car_fee[car] += max_time - dic[car]
        else:
            car_fee[car] = max_time - dic[car]    
    car_fee = sorted(car_fee.items(), key = lambda x : x[0])
    # print(car_fee)
    for cars in car_fee:
        num, time = cars
        if time > fees[0]:
            answer.append(fees[1]+ ceil( (time-fees[0]) / fees[2] ) * fees[3])
        else:
            answer.append(fees[1])
    return answer