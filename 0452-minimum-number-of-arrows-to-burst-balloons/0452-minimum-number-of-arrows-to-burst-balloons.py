class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        points.sort(key=lambda x : x[1])
        arrows = 1
        curr_end = points[0][1]

        for xstart, xend in points[1:]:
            if xstart > curr_end:
                arrows += 1
                curr_end = xend
        
        return arrows
