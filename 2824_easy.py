class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        pairs=0
        left=0
        right=len(nums)-1
        sorted_nums=sorted(nums)
        while left<right:
            if sorted_nums[left]+sorted_nums[right]<target:
                pairs+=right-left
                left+=1
            else:
                right-=1
        return pairs