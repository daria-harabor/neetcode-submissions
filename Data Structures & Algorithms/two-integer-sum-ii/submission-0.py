class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for number in numbers:
            if (target - number) in numbers:
                return [numbers.index(number)+1, numbers.index(target-number)+1]