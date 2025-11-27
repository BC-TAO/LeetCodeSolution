# classic stack question
        # why use stack?
        # When enter a (,[,{ we need },],) to close the bracket.
        
        # initialization 
        stack = []

        for i in s:
            # push when a leftside of bracket was met
            if i =='(' or i == '[' or i == '{':
                stack.append(i)
            ## the leftmost must be a left bracket so we can have a else condition here
            else:
                #  the length of s is as least 1
                if not stack:
                    return False
                # check if bracket closed
                else:
                    if i ==')' and stack.pop() !='(':
                        return False
                    elif i ==']' and stack.pop() !='[':
                        return False
                    elif i =='}' and stack.pop() !='{':
                        return False
        
        # after loop, if stack is empty, then all bracket match and return True
        return len(stack) == 0
