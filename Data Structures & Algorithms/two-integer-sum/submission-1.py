class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for each number i, sum with number j and see if it adds to target
        for i in range(len(nums)):
            for j in range (i+1, len(nums)):
                if nums[i] + nums [j] == target:
                    return [i, j]
        return []
