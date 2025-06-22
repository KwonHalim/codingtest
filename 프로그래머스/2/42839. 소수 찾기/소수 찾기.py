import itertools
import math

def solution(numbers):
    max = 10000000
    answer = 0
    answers = [True] * max
    answers[0] = answers[1] = False
    combination = set()

    for i in range(2, int(math.sqrt(max)) + 1):
        if answers[i]:
            for j in range(i * i, max, i):
                answers[j] = False

    for j in range(1, len(numbers) + 1):
        for p in itertools.permutations(numbers, j):
            num = int(''.join(p))
            print(f"{num}")
            combination.add(num)

    for num in combination:
        if answers[num]:
            print(f"정답처리:{num}")
            answer += 1

    return answer
