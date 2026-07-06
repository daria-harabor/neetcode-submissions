class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_sorted = ["" for i in range(len(strs))]

        for i in range(len(strs)):                          # a list of the sorted strings
            strs_sorted[i] = "".join(sorted(strs[i]))

        encounter = {}

        for j in range(len(strs)):
            if strs_sorted[j] in encounter:
                encounter[strs_sorted[j]].append(j)         # if have encountered the anagram before
            else:
                encounter[strs_sorted[j]] = [j]             # if haven't encountered the anagram before
        #print(encounter)

        all_anagrams = []
        
        for key_i in encounter:
            #print(encounter[key_i])
            anagram = []
            for j in range(len(encounter[key_i])):
                #print(encounter[key_i][j])
                anagram.append(strs[encounter[key_i][j]])
            all_anagrams.append(anagram)

        return all_anagrams
        