class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        my_set = set()
        for c_s in s:
            my_set.add(c_s)
        for c_t in t:
            if c_t not in my_set:
                return False
        return True