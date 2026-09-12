
nums = [1, 1, 3, 4, 2, 6, 8, 6, 7, 9, 0]

class Solution:
    def hasDuplicates (self, nums: list[int]) -> bool:
        new_sorted_nums = sorted(nums)
        return any(a == b for a,b in zip(new_sorted_nums, new_sorted_nums[1:]))

s = Solution()
print(s.hasDuplicates(nums))

