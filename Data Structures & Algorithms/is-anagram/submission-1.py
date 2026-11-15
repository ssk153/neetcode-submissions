class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sDict = {}
        tDict = {}

        for c in s:
            if c in sDict:
                sDict[c] += 1
            else:
                sDict[c] = 1
        
        for c in t:
            if c in tDict:
                tDict[c] += 1
            else:
                tDict[c] = 1

        for k,_ in sDict.items():
            if k not in tDict or sDict[k] != tDict[k]:
                return False
        return True