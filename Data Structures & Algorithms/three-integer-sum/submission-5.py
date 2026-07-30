class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #written by GPT with time complexity O(n^2)
        nums.sort()
        triplets = []
        for i in range(len(nums) - 2):
            # Avoid using the same first value more than once, use the first iteration only
            if i > 0 and nums[i] == nums[i - 1]:
                continue   # skip to the next value of i if you've encountered this value before

            # Since nums is sorted, everything afterward is also positive
            if nums[i] > 0: # three positive numbers cannot add to 0
                break       # stops the for loop alltogether

            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1   # We need a larger sum

                elif total > 0:
                    right -= 1  # We need a smaller sum

                else:
                    triplets.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]: # Skip repeated second values
                        left += 1

                    while left < right and nums[right] == nums[right + 1]: # Skip repeated third values
                        right -= 1
        return triplets