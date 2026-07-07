class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # This solution is written by GPT fully because I didn't know  
        # how to keep O(n) complexity with no division
        n = len(nums)
        output = [1] * n

        prefix = 1
        for i in range(n):
            output[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(n - 1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]

        return output