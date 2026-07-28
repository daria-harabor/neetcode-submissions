class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_length = 0
        for number in nums:
            if number - 1 not in nums:
                length = 1
                while number + 1 in nums:
                    length += 1
                    number += 1
                if length > max_length:
                    max_length = length
        return max_length