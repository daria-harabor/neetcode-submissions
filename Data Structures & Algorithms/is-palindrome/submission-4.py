class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = str()
        for char in s:
            if char.isalnum() == True:
                clean_s = clean_s + char

        reverse_clean_s = str() 
        length = len(clean_s)
        print(clean_s)

        for i in range(length):
            reverse_clean_s = reverse_clean_s + clean_s[length-i-1]
        print(reverse_clean_s)
        if reverse_clean_s.casefold() == clean_s.casefold():
            return True
        else:
            return False
        