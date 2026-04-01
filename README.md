# alg_practice
hyh daily algorithm practice
华为可信刷题日常
每日一题
争取考过可信专业级

## OJ 模板

通用模板文件：
- `alg_practice/oj_template.py`

使用方式：
- 复制 `alg_practice/oj_template.py` 到 `alg_practice/subject_list/题目名.py`
- 修改 `solve_case(...)` 实现核心算法
- 修改 `parse_input(data)` 适配题目输入
- 补充 `FIXED_TESTS`
- 如果需要随机对拍，再实现 `brute_force(...)` 和 `generate_random_case()`

运行规则：
- 直接运行文件且没有标准输入：执行本地测试
- 传入标准输入：按 OJ 模式输出结果
