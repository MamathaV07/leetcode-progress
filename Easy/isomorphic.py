class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_t = {}
        t_s = {}

        for sc, tc in zip(s, t):
            if sc in s_t:
                if s_t[sc] != tc:
                    return False
            else:
                if tc in t_s:
                    return False
                s_t[sc] = tc
                t_s[tc] = sc
        return True 