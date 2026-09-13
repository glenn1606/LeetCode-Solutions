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
        """for c in countS:
                if countS[c] != countT.get(c, 0):
                    return False
            return True"""
        ##improves by using dictionary comparison: the position of keys doesn't matter as long as they have the same number of keys and the keys match and their following values also match
        return countS==countT


o = Solution()
print(o.Anagram(s,t))