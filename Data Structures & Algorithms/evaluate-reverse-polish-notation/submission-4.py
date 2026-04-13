import operator 

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # loop thru tokens
        # map string operators to actual operation -> operator.___
        # init empty stack
        # if tokens[i] is a num:
        #   append to stack
        # elif tokens[i] is an operator:
        #   val_one = int(stack.pop()) 
        #   val_two = int(stack.pop()) 
        #   result = val_one operations[tokens[i]] val_two
        # append result to stack

        operations = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv
        }

        rpn_stack = []
 
        for i in range(len(tokens)):
            if tokens[i] in operations:
                val_one = int(rpn_stack.pop())
                val_two = int(rpn_stack.pop())
                res = operations[tokens[i]](val_two, val_one)
                rpn_stack.append(res)
            else:
                rpn_stack.append(tokens[i])
        
        return int(rpn_stack.pop())

