def solution(array, commands):
    answer = []
    arr = []
    for command in commands:
        arr = array[command[0]-1:command[1]:1]
        arr.sort()
        answer.append(arr[command[2]-1])
        
        
        
    return answer