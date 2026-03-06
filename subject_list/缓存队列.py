from typing import List, Tuple
import math
from collections import deque

class Solution:
    
    def memory_with_write_buffer(self, buffer_cap: int, operations: List[Tuple[int, int, int, int]], data: str) -> str:
        data_list = list(data)
        buffers = deque()
        data_to_write = [0] * (len(data) // 2)
        for operation in operations:
            op = operation[0]
            offset = operation[1]
            length = operation[2]
            content = operation[3]
            
            if op == 1:
                content = hex(content)[2:].upper()
                for _ in range(2 - len(content)):
                    content = "0" + content
                split_ops = []
                split_num = math.ceil(length / 8)
                last_length = length % 8
                i = 0
                while i < split_num:
                    if i == split_num - 1 and last_length != 0:
                        split_ops.append([op, offset + i * 8, last_length, content])
                    else:
                        split_ops.append([op, offset + i * 8, 8, content])
                    i += 1
                for split_op in split_ops:
                    if len(buffers) >= buffer_cap:
                        op_write = buffers.popleft()
                        start_idx = op_write[1] * 2
                        new_str = op_write[3] * op_write[2]
                        data_list[start_idx:start_idx + len(new_str)] = list(new_str)
                        for i in range(len(data_to_write)):
                            if data_to_write[i] != 0:
                                data_to_write[i] -= 1
                    buffers.append(split_op)
                    index = len(buffers)
                    for i in range(split_op[1], split_op[1] + split_op[2]):
                        data_to_write[i] = index            
            elif op == 2:
                indexs = set()
                for index in range(offset, offset + length):
                    if data_to_write[index] != 0:
                        indexs.add(data_to_write[index])
                if indexs:
                    max_index = max(indexs)
                    to_process = []
                    for _ in range(max_index):
                        to_process.append(buffers.popleft())
                    for op_write in to_process:
                        start_idx = op_write[1] * 2
                        new_str = op_write[3] * op_write[2]
                        data_list[start_idx:start_idx + len(new_str)] = list(new_str)
                        for i in range(len(data_to_write)):
                            if data_to_write[i] != 0:
                                data_to_write[i] -= 1
            else:
                for op_write in buffers:
                    start_idx = op_write[1] * 2
                    new_str = op_write[3] * op_write[2]
                    data_list[start_idx:start_idx + len(new_str)] = list(new_str)
                    for i in range(len(data_to_write)):
                        if data_to_write[i] != 0:
                            data_to_write[i] -= 1
                buffers.clear()
        return ''.join(data_list)


if __name__ == '__main__':
    s = Solution()
    buffer_cap = 5
    operations = [[1, 35, 2, 100], [1, 0, 40, 255], [1, 11, 10, 81], [1, 16, 12, 173], [2, 16, 3, 0], [2, 0, 3, 0]]
    data = "00000000000000000000000000000000000000000000000000000000000000000000000000000000"
    res = s.memory_with_write_buffer(buffer_cap, operations, data)
    print(res)
    print(res == "FFFFFFFFFFFFFFFFFFFFFF5151515151ADADADADADADADADFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF")