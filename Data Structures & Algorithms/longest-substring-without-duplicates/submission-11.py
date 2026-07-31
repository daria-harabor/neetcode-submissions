class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        max_substring = 0
        while right < len(s):
            if s[right] in s[left:right]:
                left += 1
                
            else:
                right += 1
                if (right - left) > max_substring:
                    max_substring = right - left

            if right == len(s) and max_substring == 0:
                max_substring = len(s)
                

        return max_substring