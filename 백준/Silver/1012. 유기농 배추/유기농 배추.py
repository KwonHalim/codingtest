def bfs(arr):
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]

    queue = []
    cnt = 0
    for y in range(len(arr)):
        for x in range(len(arr[y])):
            if arr[y][x] == 1:
                # print(f"방문:y:{y} x:{x}")
                cnt += 1
                queue.append([x,y])
                while queue:
                    current = queue.pop(0)
                    for i in range(4):
                        mx = current[0] + dx[i]
                        my = current[1] + dy[i]
                        if(arr[my][mx] == 1 and mx < len(arr[0]) and my < len(arr)):
                            queue.append([mx,my])
                            arr[my][mx] = 0
                            # print(f"0으로 바꾼 좌표:x:{mx} y:{my}")
    return cnt



num = int(input())
for i in range(num):
    m, n, k = map(int, input().split())
    arr = [[0] * (m+1) for _ in range(n+1)]
    for j in range(k):
        x,y = map(int, input().split())
        arr[y][x] = 1
    # for i in arr:
        # print(i)
    print(bfs(arr))



