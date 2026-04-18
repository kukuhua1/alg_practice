from typing import List
class Solution:
    def execute(self, inputs: List[str], variables: List[int]) -> List[int]:
        res = []
        stack = []  
        
        i = 0
        length = len(inputs)
        while i < length:
            input = inputs[i]
            op_num = input.split(' ')
            op = op_num[0]
            if op == 'LOAD':
                num = int(op_num[1])
                stack.append(variables[num])
                i += 1
            elif op == 'STORE':
                num = int(op_num[1])
                value = stack.pop()
                variables[num] = value
                i += 1
            elif op == 'ADD':
                right = stack.pop()
                left = stack.pop()
                stack.append(left + right)
                i += 1
            elif op == 'SUBTRACT':
                right = stack.pop()
                left = stack.pop()
                stack.append(left - right)
                i += 1
            elif op == 'COMPARE':
                opname = int(op_num[1])
                right = stack.pop()
                left = stack.pop()
                if opname == 0:
                    if left < right:
                        stack.append(1)
                    else:
                        stack.append(0)
                elif opname == 2:
                    if left == right:
                        stack.append(1)
                    else:
                        stack.append(0)
                else:
                    if left > right:
                        stack.append(1)
                    else:
                        stack.append(0)
                i += 1
            elif op == 'JUMPIF':
                num = int(op_num[1])
                value = stack.pop()
                if value == 0:
                    i = num
                else:
                    i += 1
            else:
                res.append(stack.pop())
                res.extend(variables)
                break
        return res

        
a = Solution()
inputs = ["LOAD 1", "LOAD 0", "ADD", "STORE 0", "LOAD 0", "RETURN"]
variables = [2, 5]
print(a.execute(inputs, variables))