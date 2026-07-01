class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_list_s = sorted(s)
        sorted_list_t = sorted(t)
        sorted_text_s = "".join(sorted_list_s)
        sorted_text_t = "".join(sorted_list_t)
        if sorted_text_s == sorted_text_t:
            return True
        else:
            return False