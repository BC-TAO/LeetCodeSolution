class Solution:
    def removeDuplicates(self, s: str) -> str:
        # Using data structure stack
        # why using stack?
        # when peek the top of stack, if it is not adjacent duplicate, we ignore.

        #  initialization
        stack =[]
        # push the first value
        for i in s:
            # push if stack is empty or adjacent
            if not stack or stack[-1] !=i:
                stack.append(i)
            # pop when adjacent duplicates meets
            else:
                stack.pop()
        return "".join(stack)



### Solution 2 ###################
def removeDuplicates(self, S):
    return reduce(lambda s, c: s[:-1] if s[-1:] == c else s + c, S)
###################################
