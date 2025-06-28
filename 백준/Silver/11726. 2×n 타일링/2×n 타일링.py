num = int(input())
arr = [-1] * 1001
arr[0] = 0
arr[1] = 1
arr[2] = 2


for i in range(3, num + 1):
    arr[i] = arr[i - 1] + arr[i - 2]

print(arr[num] % 10007)