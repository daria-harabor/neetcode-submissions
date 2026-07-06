class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for element in strs:
            encoded = encoded + element + "."
        
        return encoded

    def decode(self, s: str) -> List[str]:
        word = ""
        decoded = []
        for i in range(len(s)):
            if s[i] == ".":
                decoded.append(word)
                word = ""
            else:
                word = word + s[i]

        return decoded