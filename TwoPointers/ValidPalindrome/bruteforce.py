s = "Was it a car or a cat I saw?"

class Solution:
    def ValidPalindrome(self, s:str) -> bool:
        j = len(s)-1
        i = 0
        while i < j:
            ##neu khong phai ki tu hoac chu so thi tang con tro
            while i<j and not s[i].isalnum():
                i+=1
            while i<j and not s[j].isalnum():
                j-=1
            #so sanh 2 ki tu o 2 dau pointer
            if s[i].lower() != s[j].lower():
                return False

            i+=1
            j-=1
        return True

p = Solution()
print(p.ValidPalindrome(s))
