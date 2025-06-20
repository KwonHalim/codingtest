def cal_time(sch_time, actual_time):
    sch_total_minutes = (sch_time // 100) * 60 + (sch_time % 100)
    actual_total_minutes = (actual_time // 100) * 60 + (actual_time % 100)
    allowed_total_minutes = sch_total_minutes + 10 
    return actual_total_minutes > allowed_total_minutes
    
    
    
def solution(schedules, timelogs, startday):
      
    person = len(schedules)
    success = [1] * person 
    answer = 0
    if startday == 7: 
        for i_person in range(person):
            for j_day_idx in range(1, 6): 
                if(cal_time(schedules[i_person], timelogs[i_person][j_day_idx])):
                    success[i_person] = 0

    else:
        for i_person in range(person):
            for j_idx1 in range(6 - startday):
                if(cal_time(schedules[i_person], timelogs[i_person][j_idx1])):
                    success[i_person] = 0
                    break

            if success[i_person] == 0:
                continue 
            for j_idx2 in range(8 - startday, 7):
                if(cal_time(schedules[i_person], timelogs[i_person][j_idx2])):
                    success[i_person] = 0
                    break

    for status in success: 
        if status == 1:
            answer += 1

    return answer

