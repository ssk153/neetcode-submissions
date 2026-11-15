class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0

        hset = set(nums)
        for n in hset:
            if n-1 not in hset:
                current = n
                count = 1

                while current+1 in hset:
                    current += 1
                    count += 1
                longest = max(longest, count)
        return longest
        

