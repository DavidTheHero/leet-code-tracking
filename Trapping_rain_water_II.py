class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        import heapq
        m,n = len(heightMap), len(heightMap[0])
        visited = [[False]*n for _ in range(m)]
        heap = []
        for c in range(n):
            heapq.heappush(heap, (heightMap[0][c], 0, c))
            heapq.heappush(heap, (heightMap[m-1][c], m-1, c))
            visited[0][c] = True
            visited[m-1][c] = True
        for r in range(1, m-1):
            heapq.heappush(heap, (heightMap[r][0], r, 0))
            heapq.heappush(heap, (heightMap[r][n-1], r, n-1))
            visited[r][0] = True
            visited[r][n-1] = True
        trapped = 0
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]
        water_level = 0
        while heap:
            h, r, c = heapq.heappop(heap)
            water_level = max(water_level, h)
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                    visited[nr][nc] = True
                    nh = heightMap[nr][nc]
                    if nh < water_level:
                        trapped += water_level - nh
                    heapq.heappush(heap, (max(nh, water_level), nr, nc))
        return trapped
        
heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
print(Solution().trapRainWater(heightMap))