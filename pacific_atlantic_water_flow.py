class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        from collections import deque
        m, n = len(heights), len(heights[0])
        def bfs(starts):
            q = deque(starts)
            seen = [[False]*n for _ in range(m)]
            for r, c in starts:
                seen[r][c]= True
            dirs = [(-1,0),(1,0),(0,-1),(0,1)]
            while q:
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and not seen[nr][nc]:
                        if heights[nr][nc] >= heights[r][c]:
                            seen[nr][nc] = True
                            q.append((nr,nc))
            return seen
        pac_starts = [(0, c) for c in range(n)] + [(r, 0) for r in range(m)]
        atl_starts = [(m-1, c) for c in range(n)] + [(r, n-1) for r in range(m)]
        pac = bfs(pac_starts)
        atl = bfs(atl_starts)
        res = []
        for r in range(m):
            for c in range(n):
                if pac[r][c] and atl[r][c]:
                    res.append([r, c])
        return res
        
heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
print(Solution().pacificAtlantic(heights))