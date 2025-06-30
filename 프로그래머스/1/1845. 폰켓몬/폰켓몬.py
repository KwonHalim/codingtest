from itertools import combinations

def solution(nums):
    com = set(nums)
    if len(com) < len(nums)//2:
        return len(com)
    else:
        return len(nums)//2