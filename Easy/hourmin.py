class Solution:
    def findLatestTime(self, s: str) -> str:
        time = list(s)

        if time[0] == '?':
            if time[1] =='?':
                time[0] = '1'
                time[1] = '1'
            elif '0' <= time[1] <='1':
                time[0] = '1'
            else:
                time[0] = '0'

        if time[1] == '?':
            if time[0] =='1':
                time[1] = '1'
            else:
                time[1] = '9'
                w
        if time[3] == '?':
            time[3] = '5'
        if time[4] == '?':
            time[4] = '9'
        return ''.join(time)