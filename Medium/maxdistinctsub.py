class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        l = 0
        r = 0
        current_sum = 0
        max_sum = 0
        seen = set()
        while r < len(nums):
            while nums[r] in seen:
                seen.remove(nums[l])
                current_sum -= nums[l]
                l += 1
            seen.add(nums[r])
            current_sum += nums[r]
            if r - l + 1 == k:
                max_sum = max(max_sum, current_sum)
                seen.remove(nums[l])
                current_sum -= nums[l]
                l += 1
            r += 1
        return max_sum
