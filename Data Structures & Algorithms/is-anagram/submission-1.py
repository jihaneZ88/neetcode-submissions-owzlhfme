class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        my_dict = {}
        for c_s in s:
            if c_s in my_dict:
                my_dict[c_s] += 1
            else:
                my_dict[c_s] = 1
        for c_t in t:
            if c_t not in my_dict:
                return False
            if my_dict[c_t] == 0:
                return False
            my_dict[c_t] -= 1
        return True