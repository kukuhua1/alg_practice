from collections import deque

def min_dist(matrix):
    m, n = len(matrix), len(matrix[0])
    dists = [[-1] * n for _ in range(m)]
    
    q = deque()
    warehouses = 0
    stores = 0

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0: # warehouse
                dists[i][j] = 0
                q.append((i, j)) 
                warehouses += 1
            elif matrix[i][j] == 1: # store
                stores += 1
    if warehouses == 0 or stores == 0:
     return 0
    
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while q:
        x, y = q.popleft()
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n:
                if matrix[nx][ny] == 1 and dists[nx][ny] == -1:
                    dists[nx][ny] = dists[x][y] + 1
                    q.append((nx, ny))
    ans = 0
    for i in range(m):
        for j in range(n):
            if dists[i][j] != -1 and matrix[i][j] != -1:
                ans += dists[i][j]
    return ans



if __name__ == '__main__':
    matrix = [
    [1, -1, 0],
    [0, 1, 1],
    [1, -1, 1]
    ]
    print(min_dist(matrix))
