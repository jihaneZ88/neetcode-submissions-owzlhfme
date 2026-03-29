class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_map = {}
        i_j = []
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in my_map:
                i_j.append(my_map[diff])
                i_j.append(i)
                break;
            else:
                my_map[nums[i]] = i
        return i_j
        