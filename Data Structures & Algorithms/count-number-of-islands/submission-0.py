class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_island=0
        directions= [[0,1], [0,-1], [1,0], [-1,0]]
        def dfs(r,c):
            if r<0 or r>=len(grid) or c<0 or c>=len(grid[0]) or grid[r][c] == "0":
                return
            grid[r][c]="0"
            left= dfs(r,c-1)
            right=dfs(r,c+1)
            up=dfs(r+1,c)
            down=dfs(r-1,c)

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    num_island+=1
                    dfs(i,j)

        return num_island