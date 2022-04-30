ar = [[0 for j in range(10)] for i in range(10)]
ans = 1

def dfs(x, y, cur):
    global ans
    mx = -1

    if(0 < x and ar[x-1][y] < ar[x][y]): mx = max(mx, ar[x-1][y])
    if(0 < y and ar[x][y-1] < ar[x][y]): mx = max(mx, ar[x][y-1])
    if(y < m-1 and ar[x][y+1] < ar[x][y]): mx = max(mx, ar[x][y+1])
    if(x < n-1 and ar[x+1][y] < ar[x][y]): mx = max(mx, ar[x+1][y])

    if(0 < x and ar[x-1][y] == mx): dfs(x-1, y, cur+1)
    if(0 < y and ar[x][y-1] == mx): dfs(x, y-1, cur+1)
    if(y < m-1 and ar[x][y+1] == mx): dfs(x, y+1, cur+1)
    if(x < n-1 and ar[x+1][y] == mx): dfs(x+1, y, cur+1)

    ans = max(ans, cur+1)

n, m = map(int, input().split(','))
ar = [list(map(int, input().split(','))) for i in range(n)]

x, y = map(int, input().split(','))

dfs(x-1, y-1, 0)

print(ans)
