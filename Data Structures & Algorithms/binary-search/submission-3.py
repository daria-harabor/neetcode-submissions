class Solution:
    def search(self, nums: List[int], target: int) -> int:
        position = 0
        length = len(nums)

        while length > 0:
            half = length // 2
            mid = position + half

            if target == nums[mid]:
                return mid

            elif target > nums[mid]:
                position = mid + 1
                length = length - half - 1

            else:
                length = half

        return -1

        