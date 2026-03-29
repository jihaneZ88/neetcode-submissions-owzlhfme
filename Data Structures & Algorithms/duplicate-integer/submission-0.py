class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_set = set()
        for i in range(len(nums)):
            my_set.add(nums[i])
        if len(my_set) < len(nums):
            return True
        return False