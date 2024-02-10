# https://www.codingninjas.com/studio/problems/find-character-case_58513?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTabValue=SUBMISSION

char = input()
def check(char):
    if char.isupper():
        return 1
    elif char.islower():
        return 0
    else:
        return -1

print(check(char))
