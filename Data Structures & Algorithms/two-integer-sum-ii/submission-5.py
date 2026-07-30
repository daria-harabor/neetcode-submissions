class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            if numbers[left] + numbers[right] > target: # too big
                right -= 1

            elif numbers[left] + numbers[right] < target: # too small
                left += 1

            else:   # spot on!
                return [left + 1, right + 1]
                # break -> no need for it because the return already exits the function
        
    # Time Complexity: O(n)
    # Space Complexity: O(1)

                
        