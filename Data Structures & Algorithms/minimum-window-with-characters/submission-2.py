class Solution:
    def minWindow(self, s: str, t: str):
        if t=="":
            return ""
        t_dict = {}
        for ch in t:
            t_dict[ch] = t_dict.get(ch, 0) + 1
        minLen=float('inf')
        res=[-1, -1]
        s_dict={}
        def valid():
            for ch in t_dict:
                if t_dict[ch]>s_dict.get(ch, 0):
                    return False
            return True
        i=0
        while i<len(s) and s[i] not in t_dict:
            i+=1
        for j in range(i, len(s)):
            s_dict[s[j]] = s_dict.get(s[j], 0)+1

            while valid():
                if s[i] in s_dict:
                    s_dict[s[i]]-=1
                    if s_dict[s[i]]==0:
                        del s_dict[s[i]]
                if j-i+1<minLen:
                    minLen=j-i+1
                    res=[i, j+1]
                i+=1
                while i<len(s) and s[i] not in t_dict:
                    i+=1
        if res!=[-1, -1]:
            return s[res[0]: res[1]]
        else:
            return ""

        