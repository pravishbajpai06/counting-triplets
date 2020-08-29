'''You are given an array and you need to find number of tripets of indices(i,j,k)  
such that the elements at those indices are in geometric progression for a given common ratio r and i<j<k .
For example arr=[1,4,16,64], If r=4 . , we have[1,4,16]  and [4,16,64] at indices(0,1,2)  and (1,2,3) .'''

import math
import os
import random
import re
import sys
from collections import Counter
from collections import defaultdict

# Complete the countTriplets function below.
def countTriplets(arr, ratio):
    r = Counter(arr[1:]) #right side
    l = defaultdict(int) #left side
    c = 0
    for i in range(len(arr)):
        if i!=0:
            l[arr[i-1]]+=1
            r[arr[i]]-=1
        c += l[arr[i]/ratio]*r[arr[i]*ratio]
    return c          



