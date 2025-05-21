class Solution:
    def findLHS(self, nums: List[int]) -> int:

        count = Counter(nums)
        maximum_len = 0

        for num in count:

            if num+1 in count:
                group_size = count[num] + count[num+1]

                maximum_len = max(maximum_len, group_size)

        return maximum_len
        