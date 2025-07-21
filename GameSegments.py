#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'playSegments' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY coins as parameter.
#

def playSegments(coins):
    # Write your code here
    total=sum((1 if c==1 else -1) for c in coins)
    prefix=0
    if prefix*2>total:
        return 0
    for i,c in enumerate(coins):
        prefix+=(1 if c==1 else -1)
        if prefix*2>total:
            return i+1
    return -1    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    coins_count = int(input().strip())

    coins = []

    for _ in range(coins_count):
        coins_item = int(input().strip())
        coins.append(coins_item)

    result = playSegments(coins)

    fptr.write(str(result) + '\n')

    fptr.close()
