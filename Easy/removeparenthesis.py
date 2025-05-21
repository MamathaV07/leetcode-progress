class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = ""
        count = 0
        temp = ""
        
        for ch in s:
            if ch == '(':
                if count > 0:
                    temp += ch
                count += 1
            else:
                count -= 1
                if count > 0:
                    temp += ch
                else:
                    result += temp
                    temp = ""
        return result
