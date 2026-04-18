def calculate_total_task_time(task_flow):
    """
    计算任务流的总执行耗时（完全适配非串行依赖+前置时间+通道串行规则）
    :param task_flow: 任务流列表，格式如[['A',-1], ['A',-1], ['B',-1], ['C',2]]
    :return: 所有任务执行完毕的总耗时
    """
    # 1. 基础配置：任务类型→通道映射、任务类型→耗时映射
    task_to_channel = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'F': 5}
    task_duration = {'A': 10, 'B': 12, 'C': 17, 'D': 9, 'F': 5}
    
    # 2. 任务建模：初始化每个任务的核心信息
    task_info = []
    for idx, (task_type, pre_idx) in enumerate(task_flow):
        
        task_info.append({
            'idx': idx,                # 任务流索引
            'type': task_type,         # 任务类型
            'pre_idx': pre_idx,        # 前置任务索引
            'channel': task_to_channel[task_type],  # 所属通道
            'duration': task_duration[task_type],   # 耗时
            'start_time': None,        # 开始时间
            'end_time': None,          # 结束时间
            'completed': False         # 是否完成
        })
    
    # 3. 初始化状态：通道可用时间（通道下一个任务可开始的最早时间）
    channel_available_time = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
    total_tasks = len(task_info)
    completed_count = 0
    max_iter = total_tasks * 2  # 防止循环依赖死循环
    iter_count = 0

    # 4. 拓扑排序执行任务（核心逻辑）
    while completed_count < total_tasks and iter_count < max_iter:
        iter_count += 1
        executable_tasks = []
        
        # 步骤1：筛选当前可执行的任务（前置完成+未执行）
        for task in task_info:
            if task['completed']:
                continue
            
            # 检查前置依赖是否完成
            if task['pre_idx'] == -1:
                # 无前置，直接可执行
                executable_tasks.append(task)
            else:
                pre_task = task_info[task['pre_idx']]
                if pre_task['completed']:
                    # 前置已完成，可执行
                    executable_tasks.append(task)
        
        # 步骤2：检测循环依赖
        if not executable_tasks and completed_count < total_tasks:
            raise ValueError("任务流存在循环依赖，无法执行完成")
        
        # 步骤3：按通道分组，同一通道内按索引升序（保证索引靠前优先）
        from collections import defaultdict
        channel_task_group = defaultdict(list)
        for task in executable_tasks:
            channel_task_group[task['channel']].append(task)
        
        # 步骤4：执行每个通道的可执行任务（核心：开始时间=max(通道可用时间, 前置结束时间)）
        for channel, tasks in channel_task_group.items():
            # 同一通道内按索引升序执行
            tasks_sorted = sorted(tasks, key=lambda x: x['idx'])
            
            for task in tasks_sorted:
                # 计算前置任务的结束时间（无前置则为0）
                if task['pre_idx'] == -1:
                    pre_end_time = 0
                else:
                    pre_end_time = task_info[task['pre_idx']]['end_time']
                
                # 任务开始时间 = max(通道可用时间, 前置结束时间)
                task['start_time'] = max(channel_available_time[channel], pre_end_time)
                # 任务结束时间 = 开始时间 + 耗时
                task['end_time'] = task['start_time'] + task['duration']
                
                # 更新通道可用时间（下一个任务需等当前任务结束）
                channel_available_time[channel] = task['end_time']
                # 标记任务完成
                task['completed'] = True
                 

                 
                completed_count += 1

    # 最终校验：是否因循环依赖未完成
    if completed_count < total_tasks:
        raise ValueError(f"执行{max_iter}次后仍有{total_tasks-completed_count}个任务未完成，疑似循环依赖")
    
    # 总耗时 = 所有任务结束时间的最大值
    total_time = max(task['end_time'] for task in task_info) if task_info else 0
    return total_time


# -------------------------- 验证所有测试用例 --------------------------
if __name__ == "__main__":
    # 测试示例1：原题目示例（预期29）
    test_flow1 = [['A', -1], ['A', -1], ['B', -1], ['C', 2]]
    print(f"测试示例1总耗时：{calculate_total_task_time(test_flow1)}")  # 输出29（正确）
    
    # 测试示例2：多依赖+多通道并行（预期36）
    test_flow2 = [['A', -1], ['B', -1], ['C', 0], ['D', 1], ['F', 3], ['A', 4]]
    print(f"测试示例2总耗时：{calculate_total_task_time(test_flow2)}")  # 输出36（正确）
    
    # 测试示例3：空任务流（预期0）
    test_flow3 = []
    print(f"测试示例3总耗时：{calculate_total_task_time(test_flow3)}")  # 输出0（正确）
    
    # 测试示例4：非串行依赖（预期38）
    test_flow4 = [['A', -1], ['B', -1], ['C', 3], ['D', 1], ['F', 1], ['A', 4]]
    print(f"测试示例4总耗时：{calculate_total_task_time(test_flow4)}")  # 输出38（正确）