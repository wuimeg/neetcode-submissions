# solution: hash set length comparison 
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numsSet = set()
        numsSet.update(nums)

        if len(numsSet) == len(nums):
            return False
        return True


        