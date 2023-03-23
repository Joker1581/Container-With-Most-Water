class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r, max_a = 0, len(height) - 1, 0
        while l < r:
            area = (r - l)*min(height[r], height[l])
            max_a = max(area, max_a)
            if height[l] >= height[r]:
                r -= 1
            else:
                l += 1
        return max_a