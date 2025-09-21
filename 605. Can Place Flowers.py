class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n==0: #always check constraints!!
            return True
        for i in range(len(flowerbed)):
            if (flowerbed[i]==0 and (i==0 or flowerbed[i-1]==0) and (i+1==len(flowerbed) or flowerbed[i+1]==0)):
                n=n-1
                flowerbed[i]=1
                if n==0:
                    return True
        return False
