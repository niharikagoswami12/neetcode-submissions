class Solution:
    def minWindow(self, s: str, t: str):
        if t=="":
            return ""
        t_dict = {}
        for ch in t:
            t_dict[ch] = t_dict.get(ch, 0) + 1
        minLen=float('inf')
        res=[-1, -1]
        
        for i in range(len(s)):
            s_dict={}
            for j in range(i, len(s)): 
                s_dict[s[j]]=s_dict.get(s[j], 0)+1

                flag=True
                for ch in t_dict:
                    if t_dict[ch]>s_dict.get(ch, 0):
                        flag=False
                        break
                if flag and (j-i+1)<minLen:
                    minLen=j-i+1
                    res=[i, j]
        if minLen != float('inf'):
            return s[res[0]:res[1]+1]
        else:
            return ""
        