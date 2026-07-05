class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq={}
        for s in strs:
            if "".join(sorted(s)) in freq:
                freq["".join(sorted(s))].append(s)
            else:
                freq["".join(sorted(s))]=[s]
        return list(freq.values())

        