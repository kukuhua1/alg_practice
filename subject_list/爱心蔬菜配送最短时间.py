import ast
import random
import sys
from functools import lru_cache


def min_delivery_hours(num, communities):
    """
    返回完成所有社区配送所需的最短小时数。

    你平时只需要修改这个函数里的算法即可，下面的 OJ 输入输出和测试框架可以直接复用。
    当前提供的是可通过该题的参考实现。
    """
    if not communities:
        return 0

    left = max(communities)
    right = sum(communities)

    def can_finish_within(limit):
        volunteers_used = 1
        current_sum = 0

        for families in communities:
            if current_sum + families <= limit:
                current_sum += families
            else:
                volunteers_used += 1
                current_sum = families
                if volunteers_used > num:
                    return False

        return True

    while left < right:
        mid = (left + right) // 2
        if can_finish_within(mid):
            right = mid
        else:
            left = mid + 1

    return left




def parse_input(data):
    lines = [line.strip() for line in data.splitlines() if line.strip()]
    if len(lines) < 2:
        raise ValueError("输入格式应为两行：第一行 num，第二行 communities 数组")

    num = int(lines[0])
    communities_text = "".join(lines[1:])
    communities = ast.literal_eval(communities_text)

    if not isinstance(communities, list):
        raise ValueError("communities 必须是列表，例如 [40, 10, 20]")

    return num, communities


def solve(data=None):
    if data is None:
        data = sys.stdin.read()

    num, communities = parse_input(data)
    return str(min_delivery_hours(num, communities))


def brute_force(num, communities):
    """
    小数据校验用暴力解。
    只用于本地测试，不用于 OJ。
    """
    n = len(communities)
    if n == 0:
        return 0

    parts = min(num, n)
    prefix_sum = [0]
    for value in communities:
        prefix_sum.append(prefix_sum[-1] + value)

    @lru_cache(None)
    def dfs(start, remain_parts):
        if remain_parts == 1:
            return prefix_sum[n] - prefix_sum[start]

        best = float("inf")
        current_sum = 0
        end_limit = n - remain_parts

        for end in range(start, end_limit + 1):
            current_sum += communities[end]
            next_best = dfs(end + 1, remain_parts - 1)
            best = min(best, max(current_sum, next_best))

        return best

    return dfs(0, parts)


def run_fixed_tests():
    test_cases = [
        (2, [40, 10, 20], 40),
        (2, [1, 1, 6, 2], 8),
        (3, [1, 2, 3, 4, 5], 6),
        (10, [3, 1, 4], 4),
        (1, [7, 2, 5], 14),
        (4, [9, 1, 1, 9], 9),
        (2, [5, 5, 5, 5], 10),
    ]

    for index, (num, communities, expected) in enumerate(test_cases, start=1):
        actual = min_delivery_hours(num, communities)
        assert actual == expected, (
            f"固定测试 {index} 失败: num={num}, communities={communities}, "
            f"expected={expected}, actual={actual}"
        )


def run_random_tests(rounds=200):
    for index in range(1, rounds + 1):
        n = random.randint(1, 8)
        num = random.randint(1, 8)
        communities = [random.randint(1, 10) for _ in range(n)]

        expected = brute_force(num, communities)
        actual = min_delivery_hours(num, communities)

        assert actual == expected, (
            f"随机测试 {index} 失败: num={num}, communities={communities}, "
            f"expected={expected}, actual={actual}"
        )


def run_tests():
    run_fixed_tests()
    run_random_tests()
    print("All tests passed.")


if __name__ == "__main__":
    if sys.stdin.isatty():
        run_tests()
    else:
        input_data = sys.stdin.read()
        if input_data.strip():
            print(solve(input_data))
        else:
            run_tests()
