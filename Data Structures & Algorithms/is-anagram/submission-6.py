class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freq=[0]*26
        for i in range(len(s)):
            freq[ord(s[i])-ord('a')]+=1
        for i in range(len(t)):
            if freq[ord(t[i])-ord('a')] != 0:
                freq[ord(t[i])-ord('a')] -=1
            else:
                return False
        return True
        