#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'maximumOccurringCharacter' function below.
#
# The function is expected to return a CHARACTER.
# The function accepts STRING text as parameter.
#

def maximumOccurringCharacter(text):
    # Write your code here
    if not text:
        return ''
    mp={}
    n=len(text)
    op=''
    count=0
    for i in range(n):
        if text[i] in mp:
            mp[text[i]]+=1
        else:
            mp[text[i]]=1
        if mp[text[i]]>count:
            op=text[i]
            count=mp[text[i]]
    return op
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    text = input()

    result = maximumOccurringCharacter(text)

    fptr.write(str(result) + '\n')

    fptr.close()
