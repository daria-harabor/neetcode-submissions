class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for element in strs:
            encoded = encoded + str(len(element)) + "#" + element 
        
        return encoded
      
    def decode(self, s: str) -> List[str]:
        decoded = []
        while len(s)>0:
            for i in range(len(s)):
                if s[i] == "#":
                    word_length = int(s[:i])
                    decoded.append(s[i + 1 : i + word_length + 1])
                    s = s[i + word_length + 1:]  # delete the word you just added to the list
                    break
        print(decoded)
        return decoded