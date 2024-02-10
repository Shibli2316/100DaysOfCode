# https://www.codingninjas.com/studio/problems/data-type_8357232?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf

from typing import *

type = input()

def dataTypes(type: str):
    data = {
        "Integer" : 4,
        "Long" : 8,
        "Float" : 4,
        "Double" : 8,
        "Character" : 1,
    }

    return data[type]

print(dataTypes(type))