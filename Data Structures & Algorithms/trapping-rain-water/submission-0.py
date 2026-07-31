class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        left = 0
        right = len(height) - 1
        left_max = height[0]
        right_max = height[len(height) - 1]

        while left < right:
            if left_max <= right_max:
                left += 1
                if height[left] > left_max:
                    left_max = height[left]     #update with new left maximum
                else:
                    water = water + min(left_max, right_max) - height[left]

            elif left_max > right_max:
                right -= 1
                if height[right] > right_max:
                    right_max = height[right]   #update with new right maximum
                else:
                    water = water + min(left_max, right_max) - height[right]
        return water

            