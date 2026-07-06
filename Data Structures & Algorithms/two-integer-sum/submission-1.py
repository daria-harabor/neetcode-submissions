class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        encounter = {}
        state = False

        for i in range(len(nums)):
            
            for key,value in encounter.items():
                if value == target - nums[i]:
                    return [key,i]
                    state = True
                    break
                    
            if state == False:
                encounter[i] = nums[i]
            else:
                break
                    
                

