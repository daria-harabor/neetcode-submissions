class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zeros = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                product *= nums[i]
            else:
                zeros += 1
        
        print(product)
        print(zeros)

        output = []

        for j in range(len(nums)):
            if (nums[j] != 0 and zeros > 0) or (nums[j] == 0 and zeros > 1):
                output.append(0)
            if nums[j] != 0 and zeros == 0:
                output.append(product // nums[j])
            if nums[j] == 0 and zeros == 1:
                output.append(product)

        return output