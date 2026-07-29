class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets_set = set()
        nums.sort()   #because the set cannot tell the difference between (1,1,2) and (1,2,1)
        for (i, number_i) in enumerate(nums):
            target = - number_i
            for (j, number_j) in enumerate (nums[i+1:], start = i+1):
                    if (target - number_j) in nums[j+1:]:
                        number_k = target - number_j
                        triplets_set.add((number_i, number_j, number_k))    
        triplets_list = []
        for triplet in triplets_set:
            triplets_list.append(list(triplet))

        return triplets_list         