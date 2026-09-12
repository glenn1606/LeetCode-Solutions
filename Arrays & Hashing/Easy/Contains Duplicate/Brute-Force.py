
nums = [1, 1, 3, 4, 2]


class Solution:

    def hasDuplicates(self, nums : list[int]) -> bool:
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] == nums [j]:
                    return True
        return False


s = Solution()
print(s.hasDuplicates(nums))  
