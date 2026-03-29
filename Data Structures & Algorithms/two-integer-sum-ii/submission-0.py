class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        arr = []
        left, right = 0, len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] == target:
                arr.append(left + 1)
                arr.append(right + 1)
                break;
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1
        return arr