s="racecar"
t="carrace"

class Solution:
    def Anagram(self, s:str, t:str) -> bool:
        return sorted(s) == sorted(t)

o = Solution()
print(o.Vanagram(s,t))