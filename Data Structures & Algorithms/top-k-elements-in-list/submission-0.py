class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}

        for i in range(len(nums)):
            if nums[i] in frequency:
                frequency[nums[i]] += 1
            else:
                frequency[nums[i]] = 1
            
        sorted_frequency = dict(sorted(frequency.items(), key = lambda item: item[1]))

        length = len(frequency) - k
        for key in list(sorted_frequency)[:length]:
            del sorted_frequency[key]
        
        popular_numbers = []
        for i in sorted_frequency:
            popular_numbers.append(i)
        
        return popular_numbers

        

#nums = [1,2,2,3,4,5,5,5,6,7,7,8,8,8,8]
#k = 2

#sol = Solution()
#print(sol.topKFrequent(nums, k))