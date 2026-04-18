


def iland_nums(grid):
    ans = 0
    rows, cols = len(grid), len(grid[0]) 
    visited = [[-1] * cols for _ in range(rows)]

    def dfs(x, y):
        # visited[x][y] = 1
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <=nx < rows and 0 <= ny < cols:
                if visited[nx][ny] == -1 and grid[nx][ny] == 1:
                    visited[nx][ny] = 1
                    dfs(nx, ny)
                    
    for i in range(rows):
        for j in range(cols):
            if visited[i][j] == -1 and grid[i][j] == 1:
                ans += 1
                visited[i][j] = 1
                dfs(i, j)
    return ans

    

