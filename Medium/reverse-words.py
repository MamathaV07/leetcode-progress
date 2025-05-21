class Solution:
    def reverseWords(self, s: str) -> str:
        result = []
        temp_word = []
        i = len(s) - 1

        while i >= 0:
            if s[i] != " ":
                temp_word.append(s[i])
            elif temp_word:
                result += temp_word[::-1]
                result.append(" ")
                temp_word = []
            i -= 1

        if temp_word:
            result += temp_word[::-1]
        while result and result[-1] == " ":
            result.pop()
        return "".join(result)