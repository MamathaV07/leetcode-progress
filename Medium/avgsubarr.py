class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        n = len(arr)
        l = 0
        current_sum = 0
        count = 0
        target = k * threshold
        while l < k:
            current_sum += arr[l]
            l += 1
        if current_sum >= target:
            count += 1
        r = k
        while r < n:
            current_sum += arr[r]        
            current_sum -= arr[r - k]    
            if current_sum >= target:
                count += 1 
            r += 1
        return count