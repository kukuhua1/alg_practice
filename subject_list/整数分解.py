# n_value 要分解的整数
# k_value 分解的项数
# p_value 指数

import math

def integer_decompose_ii(n_value, k_value, p_value):
    max_base = int(math.pow(n_value, 1 / p_value)) # 最大底数
    pow_list = [i ** p_value for i in range(max_base + 1)] # 可以分解的项 底数**p_value
    best_sum = -1
    best_list = []

    def backtrack(left_n_value, left_k_value, path, cur_sum, start_index):
        '''
        left_n_value 整数和减去当前已经相加的项还剩多少
        left_k_value 总项数减去已经相加的项还剩多少项
        path         已经check过的底数
        cur_sum      当前的底数和
        start_index  最开始的底数值，从最大值开始遍历，符合题目排序规则
        '''
        nonlocal best_sum, best_list
        # 剪枝
        if left_n_value < left_k_value:
            return
        if left_n_value > left_k_value * pow_list[start_index]:
            return
        # 选够了k_value个底数
        if left_k_value == 0 and left_n_value == 0:
            if cur_sum > best_sum or (cur_sum == best_sum and path > best_list):
                best_sum = cur_sum
                best_list = path[:]
            return
        for index in range(start_index, 0, -1):
            cur_pow = pow_list[index]
            if cur_pow > left_n_value:
                continue
            new_left_n = left_n_value - cur_pow
            new_left_k = left_k_value - 1
            # 再次剪枝
            if new_left_n < new_left_k:
                continue
            if new_left_n > new_left_k * pow_list[index]:
                continue
            # 选index
            path.append(index)
            backtrack(new_left_n, new_left_k, path, cur_sum + index, index)
            # 不选index
            path.pop()
    backtrack(n_value, k_value, [], 0, max_base)
    return best_list


if __name__ == "__main__":
    print(integer_decompose_ii(169, 5, 2))  # [6, 6, 6, 6, 5]