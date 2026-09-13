s="anagram"
t="nagaram"
class Solution:
    def Anagram(self, s:str, t:str) -> bool:
        if len(s) != len (t):
            return False
        countS, countT = {},{}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i],0)
            countT[t[i]] = 1 + countT.get(t[i],0)
        for c in countS:
            if countS[c] != countT[c]:
                return False
            return True


o = Solution()
print(o.Anagram(s,t))