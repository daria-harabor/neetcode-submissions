class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        state = False
        for i in range(len(nums)):
            if nums[i] in seen:
                state = True
                break
            seen.add(nums[i])
        return state
