class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #efficient solution, time and space complexity O(n) using Hashsets.
        store=set(nums)
        longest=0
        for num in store:
            if num-1 not in store:
                num+=1
                length=1
                while num in store:
                    length+=1
                    num+=1
                longest=max(longest,length)
        return longest

        '''if not nums:
            return 0
        res = 0
        nums.sort()
        
        curr, streak = nums[0], 0
        i = 0
        while i < len(nums):
            if curr != nums[i]:
                curr = nums[i]
                streak = 0
            while i < len(nums) and nums[i] == curr:
                i += 1
            streak += 1
            curr += 1
            res = max(res, streak)
        return res
        Time complexity: O(nlogn)
Space complexity: O(1) or O(n) depending on the sorting algorithm.
        '''
