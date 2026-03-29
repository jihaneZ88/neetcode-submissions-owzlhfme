class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sequences = defaultdict(list)
        nums_set = set(nums)
        for num in nums_set:
            if num - 1 not in nums_set:
                sequences[num].append(num)
                counter = 1
                for other in nums_set:
                    if other != num and other == num + counter:
                        sequences[num].append(other)
                        counter += 1
        print(sequences)
        return max((len(arr) for arr in sequences.values()), default=0)



        