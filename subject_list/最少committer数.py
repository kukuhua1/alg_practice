# 某代码仓配置了文件修改评审的Committer信息。
# 现有一个MR（Merge Request）修改了一批文件 files，
# files[i] 表示允许评审文件 i 的 Committer 编号列表。
# 每个文件需要至少一名Committer评审才能合入，每名Committer可以评审多个文件。
# 请计算并返回该MR最少需要多少名Committer，才能完成所有修改文件的评审？

# 贪心算法
# def min_committers(files):
#     files_to_commit = set(range(len(files)))
#     committers = set()
#     used_committer = set()
#     while files_to_commit:
#         for f in files:
#             committers.update(f)
#         max_count = 0
#         best_committer = None
#         for committer in committers:
#             if committer in used_committer:
#                 continue
#             cover_num = sum(1 for f in files if committer in f)
#             if cover_num > max_count:
#                 max_count = cover_num
#                 best_committer = committer
#         used_committer.add(best_committer)
#         uncoverd = set()
#         for file_idx in files_to_commit:
#             if best_committer not in files[file_idx]:
#                 uncoverd.add(file_idx)
#         files_to_commit = uncoverd

#     return len(used_committer)


# files = [[2, 9, 7, 1, 0, 3, 5, 8, 4], 
#          [7, 0, 2, 1, 5, 6, 4, 9],  
#          [4, 3, 7, 0, 2, 1, 8], 
#          [7], 
#          [1, 0, 9, 5, 6, 7, 2, 4, 8], 
#          [4], 
#          [5, 2, 4, 9, 1, 7], 
#          [1, 9, 8, 6, 7, 5, 0, 3], 
#          [9, 5, 8, 4, 6, 2, 0, 3, 7, 1], 
#          [4, 5, 3, 9, 0, 6, 1, 2]]

# print(min_committers(files))


# 回溯法
def min_committers_backtrack(files):
    n = len(files)
    # 把每个committer能覆盖的文件转成二进制mask
    committer_mask = {}
    for file_idx, comms in enumerate(files):
        for c in comms:
            if c not in committer_mask:
                committer_mask[c] = 0
            committer_mask[c] |= 1 << file_idx

    all_mask = (1 << n) - 1
    committers = list(committer_mask.keys())
    min_count = [len(committers)]  # 保存最小值

    # 回溯：当前选到第几个，已覆盖mask，已选人数
    def backtrack(idx, current_mask, count):
        if current_mask == all_mask:
            if count < min_count[0]:
                min_count[0] = count
            return
        if idx >= len(committers) or count >= min_count[0]:
            return
        # 选当前committer
        backtrack(idx+1, current_mask | committer_mask[committers[idx]], count+1)
        # 不选
        backtrack(idx+1, current_mask, count)

    backtrack(0, 0, 0)
    return min_count[0]


# 你的测试用例
files = [
    [2, 9, 7, 1, 0, 3, 5, 8, 4],
    [7, 0, 2, 1, 5, 6, 4, 9],
    [4, 3, 7, 0, 2, 1, 8],
    [7],
    [1, 0, 9, 5, 6, 7, 2, 4, 8],
    [4],
    [5, 2, 4, 9, 1, 7],
    [1, 9, 8, 6, 7, 5, 0, 3],
    [9, 5, 8, 4, 6, 2, 0, 3, 7, 1],
    [4, 5, 3, 9, 0, 6, 1, 2]
]

print(min_committers_backtrack(files))