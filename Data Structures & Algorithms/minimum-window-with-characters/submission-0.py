class Solution:
    def minWindow(self, s: str, t: str):

        t_dict = {}
        for ch in t:
            t_dict[ch] = t_dict.get(ch, 0) + 1

        def valid():
            for ch in t_dict:
                if s_dict.get(ch, 0) < t_dict[ch]:
                    return False
            return True

        res = [-1, -1]
        min_len = float("inf")

        i = 0
        while i < len(s) and s[i] not in t_dict:
            i += 1

        s_dict = {}

        for j in range(i, len(s)):

            if s[j] in t_dict:
                s_dict[s[j]] = s_dict.get(s[j], 0) + 1

            while valid():

                if j - i + 1 < min_len:
                    min_len = j - i + 1
                    res = [i, j]

                if s[i] in t_dict:
                    s_dict[s[i]] -= 1
                    if s_dict[s[i]] == 0:
                        del s_dict[s[i]]

                i += 1

                while i < len(s) and s[i] not in t_dict:
                    i += 1

        if res == [-1, -1]:
            return ""

        return s[res[0]:res[1] + 1]
            
        