n, m = map(int, input().split())

arr1 = [input() for _ in range(n)]

arr2_set = set(input() for _ in range(m))

answer = []

for name in arr1:
    if name in arr2_set:
        answer.append(name)

answer.sort()

print(len(answer))
for name in answer:
    print(name)