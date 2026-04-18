from typing import List
from collections import OrderedDict, defaultdict
class LoadBalanceSys:
    def __init__(self, proc_num: int, max_connect_num: int):
        self.processes = defaultdict(dict)
        self.proc_num = proc_num
        self.max_connect_num = max_connect_num
        for index in range(self.proc_num):
            self.processes[index]['status'] = False # 初始为下线状态
            self.processes[index]['procs'] = [] # 用于存储连接
            self.processes[index]['link_num'] = 0 # 记录连接数
        self.queue_dict = OrderedDict() # 记录链接和所处进程
        self.link_nums = 0 # 当前进程数
    def proc_online(self, pids: List[int]):
        for pid in pids:
            self.processes[pid]['status'] = True # 状态上线
    def proc_offline(self, pids: List[int]):
        for pid in pids:
            self.processes[pid]['status'] = False # 状态下线
            self.processes[pid]['link_num'] = 0
            # 连接队列中删除对应连接
            for proc in self.processes[pid]['procs']:
                del self.queue_dict[proc]
                self.link_nums -= 1
            self.processes[pid]['procs'] = []
    def dispatch(self, ip: int, port: int, proto: int) -> int:
        link = (ip, port, proto)
        if not self.check_status(self.processes):
            return -1
        if link in self.queue_dict: # 如果连接已经在进程了
            self.queue_dict.move_to_end(link)
            return self.queue_dict[link]
        else: # 连接不在进程
            valid_process = dict()
            for index, process in self.processes.items():
                if process['status']: # 进程上线
                    valid_process[index] = process
            sorted_processes = sorted(valid_process.items(), key=lambda x: (x[1]['link_num'], x[0]))
            index = sorted_processes[0][0] # 选择当前插入哪个进程

            self.processes[index]['procs'].append(link) # 先插入
            self.processes[index]['link_num'] += 1 # 当前进程的连接数加1
            self.queue_dict[link] = index # 入队
            if self.link_nums < self.max_connect_num:
                self.link_nums += 1 # 全局进程数加1
            else: # 最终连接数不变
                farest_link = self.queue_dict.popitem(last=False) # 弹出第一个元素，最久未被访问
                link = farest_link[0] # 弹出的连接
                link_proc = farest_link[1] # 弹出的连接所属进程
                self.processes[link_proc]['procs'].remove(link)
                self.processes[link_proc]['link_num'] -= 1 #所属进程连接数减去1
            return index

    def check_status(self, processes):  # 查看当前是否有上线的进程
        for index, proc in processes.items():
            if proc['status'] == True:
                return True
        return False





proc_num = 2 # 进程数，初始为下线状态
max_connect_num = 3 # 系统最多可保留连接数
a = LoadBalanceSys(proc_num, max_connect_num)
print(a)
print(a.proc_online([0, 1]))
print(a.dispatch(1, 2, 1))
print(a.dispatch(4, 5, 2))
print(a.dispatch(7, 5, 1))
print(a.dispatch(1, 2, 1))
print(a.dispatch(4, 5, 2))
print(a.dispatch(3, 4, 2))
print(a.dispatch(6, 8, 1))
print(a.proc_offline([1]))
print(a.dispatch(4, 5, 2))