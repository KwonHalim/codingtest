import math
# math.ceil()


def solution(fees, records):
    answer = []
    dic = {}
    park_time = {}
    for record in records:
        time, car, state = record.split(" ")
        h, m = time.split(":")
        if state == "IN":
            dic[car] = int(h)*60+int(m)
        elif state == "OUT":
            in_time = dic[car]
            park = (int(h)*60+int(m)) - in_time
            
            if car in park_time:
                park_time[car] += park
            else:
                park_time[car] = park
            
            dic.pop(car)
            
            
    for left in dic:
        time = 23*60+59 - dic[left]
        if left in park_time:
            park_time[left]+= time
        else:
            park_time[left] = time
                
    final = sorted(park_time.items())
    print(final)
#   기본 시간, 기본 요금, 단위 시간, 단위 요금
    base_time, base_fee, unit_time, unit_fee = fees
    for car_num, total_time in final:
        if total_time <= base_time:
            answer.append(base_fee)
        else:
            fee = base_fee + math.ceil((total_time - base_time) / unit_time) * unit_fee
            answer.append(fee)
    return answer