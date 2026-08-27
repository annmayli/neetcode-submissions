class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        str1 = {}
        for char in s:
            if char not in str1:
                str1[char] = 1
            else:
                str1[char] += 1

        str2 = {}
        for char in t:
            if char not in str2:
                str2[char] = 1
            else:
                str2[char] += 1
        
        if str1 == str2:
            return True
        
        return False
        
        