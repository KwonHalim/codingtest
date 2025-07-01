n = int(input())
arr = list(map(int, input().split()))

d = [-1] * n

d[0] = arr[0]

for i in range(n):
    d[i] = max(arr[i], d[i-1] + arr[i])

print(max(d))