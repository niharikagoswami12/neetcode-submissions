class Solution:

    def encode(self, strs: List[str]) -> str:
        ans=""
        for i in range(len(strs)):
            ans=ans+str(len(strs[i]))+"#"+strs[i] if i !=0 else str(len(strs[i]))+"#"+strs[i]
        return ans


    def decode(self, s: str) -> List[str]:
        res=[]
        i=0
        while i<len(s):
            j=i
            while s[j] != '#':
                j+=1
            length=s[i:j]
            i=j+1
            j=int(length)+i
            res.append(s[i:j])
            i=j
        return res

