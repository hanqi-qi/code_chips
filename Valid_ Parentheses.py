#Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#An input string is valid if:

#Open brackets must be closed by the same type of brackets.
#Open brackets must be closed in the correct order.
#Every close bracket has a corresponding open bracket of the same type.

'''example 1
Input: s = "()"
Output: true
'''

'''example 2
Input: s = "()[]{}"
Output: true
'''

'''example 3
Input: s = "()[]{}"
Output: true
'''

class Solution:
    def isValid(self, s: str) -> bool:
        result = False
        char_list = [char for char in s]
        active_list = []
        idx = 0
        while idx < len(char_list):
            active_list.append(char_list[idx])
            # print(10*"*")
            # print(idx,char_list[idx])
            # print(active_list)
            if active_list[-1] in ["]","}",")"]:
                # print("right_half")
                if len(active_list)>1 and (active_list[-2]+active_list[-1]) in ["()","[]","{}"]:
                    # print("paired!")
                    active_list = active_list[:-2]
            # print("afer processing:")
            # print(active_list)
            idx += 1
        if len(active_list) == 0:
            return True
        else:
            return False
