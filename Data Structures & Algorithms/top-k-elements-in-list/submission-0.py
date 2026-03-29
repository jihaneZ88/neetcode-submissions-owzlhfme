class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums))]
        freq = {}
        res = [] * k  
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        for num in freq:
            buckets[freq[num] - 1].append(num)
        for i in range (k):
            for num in sorted(buckets)[len(nums) - 1 - i]:
                res.append(num)
        return res