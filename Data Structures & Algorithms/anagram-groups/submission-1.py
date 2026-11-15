class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {}

        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s in hmap:
                hmap[sorted_s].append(s)
            else: 
                hmap[sorted_s] = [s]
        return list(hmap.values())