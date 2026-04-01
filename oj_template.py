import random
import sys


"""
通用 OJ 题目模板

使用方式：
1. 复制本文件到 `alg_practice/subject_list/你的题目名.py`
2. 按需修改：
   - `solve_case(...)`
   - `parse_input(data)`
   - `FIXED_TESTS`
3. 如果题目适合随机对拍，再补：
   - `brute_force(...)`
   - `generate_random_case()`

运行方式：
- 直接运行且不传标准输入：执行本地测试
- 传入标准输入：按 OJ 模式输出答案
"""


def solve_case(*args):
    """
    在这里实现题目的核心算法。

    约定：
    - `parse_input(data)` 返回什么，这里就接收什么
    - 返回值最终会被转成字符串输出
    """
    raise NotImplementedError("请先实现 solve_case(...)")


def parse_input(data):
    """
    在这里解析 OJ 输入。

    默认模板适合这类输入：
    2
    1 2 3 4

    返回值可以是：
    - 单个值，例如：nums
    - 元组，例如：(n, nums)
    """
    lines = [line.strip() for line in data.splitlines() if line.strip()]
    if not lines:
        raise ValueError("输入为空，请实现 parse_input(data)")

    n = int(lines[0])
    nums = list(map(int, lines[1].split())) if len(lines) > 1 else []
    return n, nums


def solve(data=None):
    if data is None:
        data = sys.stdin.read()

    parsed = parse_input(data)
    if isinstance(parsed, tuple):
        result = solve_case(*parsed)
    else:
        result = solve_case(parsed)
    return str(result)


def brute_force(*args):
    """
    小数据暴力解。
    如果当前题目不需要随机对拍，可以保留默认实现，不会被调用。
    """
    raise NotImplementedError("如需随机对拍，请实现 brute_force(...)")


def generate_random_case():
    """
    随机生成一组小数据。
    返回值应与 `parse_input` 的返回结构一致。
    """
    raise NotImplementedError("如需随机对拍，请实现 generate_random_case()")


# 固定样例：
# 如果 parse_input 返回 (n, nums)，这里就写成：
# ((4, [1, 2, 3, 4]), 10)
FIXED_TESTS = []


# 是否开启随机对拍
ENABLE_RANDOM_TESTS = False
RANDOM_TEST_ROUNDS = 200


def call_with_parsed_args(func, parsed):
    if isinstance(parsed, tuple):
        return func(*parsed)
    return func(parsed)


def run_fixed_tests():
    if not FIXED_TESTS:
        print("No fixed tests configured.")
        return

    for index, (parsed, expected) in enumerate(FIXED_TESTS, start=1):
        actual = call_with_parsed_args(solve_case, parsed)
        assert actual == expected, (
            f"固定测试 {index} 失败: input={parsed}, "
            f"expected={expected}, actual={actual}"
        )

    print(f"Fixed tests passed: {len(FIXED_TESTS)}")


def run_random_tests(rounds=RANDOM_TEST_ROUNDS):
    if not ENABLE_RANDOM_TESTS:
        print("Random tests skipped.")
        return

    for index in range(1, rounds + 1):
        parsed = generate_random_case()
        expected = call_with_parsed_args(brute_force, parsed)
        actual = call_with_parsed_args(solve_case, parsed)
        assert actual == expected, (
            f"随机测试 {index} 失败: input={parsed}, "
            f"expected={expected}, actual={actual}"
        )

    print(f"Random tests passed: {rounds}")


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
