class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l,r = i + 1, len(nums) - 1
            while l < r:
                curr_sum = nums[l] + nums[r]
                if curr_sum < - nums[i]:
                    l += 1
                elif curr_sum > - nums[i]:
                    r -= 1
                else:
                    res.append([nums[l], nums[r], nums[i]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res
