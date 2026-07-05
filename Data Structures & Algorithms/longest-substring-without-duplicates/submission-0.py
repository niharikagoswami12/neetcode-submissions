class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen=set()
        left=0
        max_len=0
        for i in range(len(s)):
            while s[i] in seen:
                seen.remove(s[left])
                left+=1
            seen.add(s[i])
            curr_len=i-left+1
            if max_len<curr_len:
                max_len=curr_len
        return max_len

        