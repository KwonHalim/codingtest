num = int(input())
arr = [-1] * (1000001)
arr[0] = 0
arr[1] = 0
arr[2] = 1
arr[3] = 1


for i in range(4, num+1):
    arr[i] = arr[i-1] + 1
    if i % 2 == 0:
        arr[i] = min(arr[i//2] + 1, arr[i])
    if i % 3 == 0:
        arr[i] = min(arr[i//3] + 1, arr[i])

print("정답")

for i in range(num+1):
    print(f"{i}: {arr[i]}", end = ' ')



for i in range(4, num+1):
    if i % 2 == 0:
        arr[i] = min(arr[i//2] + 1, arr[i-1] + 1)
    if i % 3 == 0:
        arr[i] = min(arr[i//3] + 1, arr[i-1] + 1)
    else:
        arr[i] = arr[i-1] + 1

print("\n내 답")

for i in range(num+1):
    print(f"{i}: {arr[i]}", end = ' ')

내 답 같은 경우에는 2,3을 모두 고려하는 것이 부족. 즉 만약 2의 배수이며 3의 배수이면서 i%2가 더 적은 횟수로 1을 만드는 상태라면 arr[i]가 arr[i-1]혹은 arr[i%3] + 1로 덮어씌어지면서 해결할 수 없음.
그리고 else 구문이 i % 3 에만 이어져 있기에 3으로 안나눠떨어지면 이것도 덮어씌어짐, 그렇다고 i % 2에 else를 둬도 위의 상황으로 해결하지 못함.
