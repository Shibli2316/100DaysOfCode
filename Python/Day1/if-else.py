# https://www.codingninjas.com/studio/problems/if-else-decision-making_8357235?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf

from typing import *

def compareIfElse(a: int, b: int):
    # Write your code here
    if a == b:
        return "equal"
    elif a > b:
        return "greater"
    else:
        return "smaller"
    
a = input()
b = input()

print(compareIfElse(a, b))