def search(self, nums: List[int], target: int) -> int:
        if len(nums)==0:
            return -1
        left,right=0,len(nums)-1
        while left<=right:
            mid=left+(right-left)//2
            if target==nums[mid]:
                return mid
            elif nums[mid]<target:
                left=mid+1
            else:
                right=mid-1
        return -1
search(nums = [-1,0,3,5,9,12], target = 2)