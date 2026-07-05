class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_s={}
        freq_t={}
        sa=list(s)
        ta=list(t)
        for si in sa:
            if si in freq_s:
                freq_s[si]+=1
            else:
                freq_s[si]=1
        for ti in ta:
            if ti in freq_t:
                freq_t[ti]+=1
            else:
                freq_t[ti]=1
        if freq_s!=freq_t:
            return False
        else:
            return True
        
        