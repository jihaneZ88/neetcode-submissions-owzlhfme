class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums) + 1)]
        freq = {}
        res = []
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        for num in freq:
            buckets[freq[num]].append(num)
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res