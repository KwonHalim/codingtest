dp_counts = [[0, 0] for _ in range(41)]

dp_counts[0][0] = 1
dp_counts[0][1] = 0

dp_counts[1][0] = 0
dp_counts[1][1] = 1

for i in range(2, 41):
    dp_counts[i][0] = dp_counts[i-1][0] + dp_counts[i-2][0]
    dp_counts[i][1] = dp_counts[i-1][1] + dp_counts[i-2][1]

num_test_cases = int(input())

for _ in range(num_test_cases):
    n = int(input())
    print(dp_counts[n][0], dp_counts[n][1])