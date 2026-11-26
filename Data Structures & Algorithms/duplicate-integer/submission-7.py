# solution: hash set --> constant time
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numsSet = set()
        for num in nums:
            # first, check if n was previously added to the set
            if num in numsSet:
                return True
            # add num to the set
            numsSet.add(num)
        return False
            
        