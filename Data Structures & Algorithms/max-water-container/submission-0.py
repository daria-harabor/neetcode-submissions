class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxim_volume = 0
        left = 0
        right = len(heights)-1

        while left < right:
            height = min(heights[left], heights[right])
            width = right - left
            if height * width > maxim_volume:
                maxim_volume = height * width

            # we can only improve the volume by increasing the height which is bound by the minimum height wall
            if heights[left] < heights[right]:
                left += 1 

            elif heights[left] > heights[right]:
                right -= 1

            else:
                left += 1
                right -= 1
        return maxim_volume