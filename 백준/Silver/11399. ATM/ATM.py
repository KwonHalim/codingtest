num = int(input())

arr = list(map(int, input().split()))


arr.sort()

total = 0
sum = 0

for i in range(num):
    sum+= arr[i]
    total = sum + total
print(total)