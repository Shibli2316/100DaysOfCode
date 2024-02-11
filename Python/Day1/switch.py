# https://www.codingninjas.com/studio/problems/switch-case-statement_8357244?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTabValue=SUBMISSION

from typing import *
import math

def areaSwitchCase(ch: int, a: List[float]):
    # Write your code here
    match ch:
        case 1:
            return f"{math.pi * a[0] * a[0]:.5f}"
        case 2:
            return f"{a[0] * a[1]:.5f}"
        case default:
            return -1