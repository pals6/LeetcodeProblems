#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'compareStrings' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def compareStrings(s1, s2):
    # Write your code here
    def removeBackSpace(string):
        stack=[]
        for i in string:
            if i!="#":
                stack.append(i)
            else:
                if len(stack):
                    stack.pop()
        return "".join(stack)
    s1,s2=removeBackSpace(s1),removeBackSpace(s2)
    return int(s1==s2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = compareStrings(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
