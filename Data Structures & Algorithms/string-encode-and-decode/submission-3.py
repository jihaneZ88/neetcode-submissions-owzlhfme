class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for string in strs:
            encoded_string += str(len(string)) + '#' + string
        return encoded_string

    def decode(self, s: str) -> List[str]:
        strs = []
        num_s = ""
        num = 0
        string = ""
        b_string = False
        for c in s:
            if c.isdigit() and b_string == False:
                num_s +=c
                continue
            elif c == '#' and b_string == False:
                b_string = True
                num = int(num_s)
                if num == 0:
                    strs.append("")
                    string = ""
                    num_s = ""
                    b_string = False
                continue
            else:
                string += c
                num -= 1
                if num == 0:
                    strs.append(string)
                    string = ""
                    num_s = ""
                    b_string = False
        return strs
