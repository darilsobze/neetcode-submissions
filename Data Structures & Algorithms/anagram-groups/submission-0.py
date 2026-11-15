class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs =[ ''.join(sorted(word)) for word in strs ]
        anagrams_dic = {}
        for i in range(len(strs)):
            anagrams_dic[sorted_strs[i]] = anagrams_dic.get(sorted_strs[i],[]) + [i]
        
        result=[]
        for anagram in anagrams_dic:
            result.append([ strs[i] for i in anagrams_dic[anagram] ])
        return result

            

        