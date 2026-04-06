class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        l,r = 0, len(nums) - 1
        for i in range(len(nums)):
            while l < r:
                curr_sum = nums[l] + nums[r]
                if curr_sum < - nums[i]:
                    l += 1
                elif curr_sum > - nums[i]:
                    r -= 1
                else:
                    res.append[[nums[l], nums[r], nums[i]]]
        return []
