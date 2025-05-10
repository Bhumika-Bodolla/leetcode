class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        mx = 0
        if len(points) <= 2:
            return len(points)
        
        for i in range(len(points) - 1):
            m = []
            for j in range(i + 1, len(points)):
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]
                
                if dx == 0:
                    dy = 'undef' 
                    m.append(dy)
                else:
                    m.append(dy / dx)
                
            mx = max(mx, m.count(max(set(m), key=m.count)) + 1) 
        
        return mx