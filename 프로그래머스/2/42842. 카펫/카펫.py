import math

def solution(brown, yellow):
    i = int(math.sqrt(yellow))
    for i in range(1, i+1):
        if yellow % i == 0:
            height = i
            width = yellow // i
            print(f"높이:{height}")
            print(f"너비:{width}")
            surround = (height * 2) + (width + 2) * 2
            print(f"갈색:{surround}")
            if surround == brown:
                return [width+2, height+2]
                
    
    