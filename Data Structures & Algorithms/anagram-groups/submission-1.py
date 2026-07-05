class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq={}
        for s in strs:
            freq1=[0]*26
            for i in range(len(s)):
                freq1[ord(s[i])-ord('a')]+=1
            if str(freq1) in freq:
                freq[str(freq1)].append(s) 
            else:
                freq[str(freq1)]=[s]
        return list(freq.values())

        