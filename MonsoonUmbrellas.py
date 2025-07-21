#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getUmbrellas' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER requirement
#  2. INTEGER_ARRAY sizes
#

def getUmbrellas(requirement, sizes):
    # Write your code here
    INF=float('inf')
    dp=[INF]*(requirement+1)
    dp[0]=0
    for i in range(1,requirement+1):
        for s in sizes:
            if s<=i and dp[i-s]!=INF:
                dp[i]=min(dp[i],dp[i-s]+1)
    return dp[requirement] if dp[requirement]!=INF else -1
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    requirement = int(input().strip())

    sizes_count = int(input().strip())

    sizes = []

    for _ in range(sizes_count):
        sizes_item = int(input().strip())
        sizes.append(sizes_item)

    result = getUmbrellas(requirement, sizes)

    fptr.write(str(result) + '\n')

    fptr.close()
