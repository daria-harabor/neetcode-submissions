class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for number in numbers:
            if (target - number) in numbers:
                i = numbers.index(number)
                if number != target - number:
                    return [i+1, numbers.index(target-number) + 1]
                else:
                    return [i+1, numbers.index(target-number, i + 1) + 1]