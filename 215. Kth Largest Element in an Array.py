class Solution:
    def partition(self,nums,left,right):
            pivot=random.randint(0, len(nums) - 1)
            store_index=left
            for i in range(left, right):
                if nums[i] <= pivot:
                    nums[store_index], nums[i] = nums[i], nums[store_index]
                    store_index += 1
            nums[store_index],nums[right]=nums[right],nums[store_index]
            return store_index
    def findKthLargest(self, nums: List[int], k: int) -> int:
        left,right=0,len(nums)-1
        t=len(nums)-k
        while True:
            p = self.partition(nums, left, right)
            if p==t:
                return nums[p]
            elif p<t:
                left=p+1
            else:
                right=p-1
        
        return nums[t]


