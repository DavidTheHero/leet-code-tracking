class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        import heapq
        n = len(grid)
        heap = [(grid[0][0], 0, 0)]
        visited = [[False]*n for _ in range(n)]
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]

        while heap:
            t, r, c = heapq.heappop(heap)
            if visited[r][c]:
                continue
            visited[r][c] = True
            if r == n-1 and c == n-1:
                return t
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                    nt = max(t, grid[nr][nc])
                    heapq.heappush(heap, (nt, nr, nc))
        return -1
    
grid = [[0,2],[1,3]]
print(Solution().swimInWater(grid))