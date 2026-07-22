class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        obj1 = {}
        obj2 = {}
        for char in s:
            if obj1.get(char, 0):
                obj1[char] += 1
            else:
                obj1[char] = 1

        for char in t:
            if obj2.get(char, 0):
                obj2[char] += 1
            else:
                obj2[char] = 1

        if obj1 == obj2:
            return True
        return False
