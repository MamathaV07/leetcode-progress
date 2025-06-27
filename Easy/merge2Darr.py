class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        value_map={}

        for id, val in nums1:
            value_map[id] = value_map.get(id, 0)+val

        for id, val in nums2:
            value_map[id] = value_map.get(id, 0)+val
            
        result = [[id, value_map[id]] for id in sorted(value_map.keys())]
        return result
