class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []
        for i in range(n+1):
            copy = i
            ones = 0
            while copy > 0:
                remainder = copy % 2
                copy = copy // 2
                if remainder == 1:
                    ones += 1
            output.append(ones)
        return output
            
