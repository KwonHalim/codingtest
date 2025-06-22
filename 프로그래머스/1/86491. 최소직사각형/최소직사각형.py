def solution(sizes):
    temp = 0
    max_w = 0
    max_h = 0
    for size in sizes:
        if(size[0] < size[1]):
            temp = size[0]
            size[0] = size[1]
            size[1] = temp
    for size in sizes:
        max_w = max(max_w, size[0])
    for size in sizes:
        max_h = max(max_h, size[1])
        
    print(f"w:{max_w}, h:{max_h}")
    
    answer = max_w * max_h

    return answer