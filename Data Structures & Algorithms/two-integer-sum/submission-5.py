class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        encounter = {}

        for i in range(len(nums)):
            
            for key,value in encounter.items():
                if value == target - nums[i]:
                    return [key,i]
                    
            encounter[i] = nums[i]
                    
                

