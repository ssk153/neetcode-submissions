# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for j in range(i, len(nums)):
#                 if nums[i] + nums[j] == target and i != j:
#                     return [i, j]
        
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in hmap:
                return [hmap[complement], i]
            else: 
                hmap[num] = i
            