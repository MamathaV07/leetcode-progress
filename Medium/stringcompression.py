class Solution:
    def compress(self, chars: List[str]) -> int:
        result = 0
        temp = 0
        while temp < len(chars):
            char = chars[temp]
            count = 0 
            while temp < len(chars) and chars[temp] == char:
                temp += 1
                count += 1
            chars[result] = char
            result += 1
            if count > 1:
                for c in str(count):
                    chars[result] = c
                    result += 1
        return result
    