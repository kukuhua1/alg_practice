from typing import List
from collections import defaultdict


class FileSystem:
    def __init__(self):
        self.current_dir = '/'
        self.file_system = defaultdict(list)
        self.file_system[self.current_dir] = []

    def _join_path(self, name: str) -> str:
        if self.current_dir.endswith('/'):
            return self.current_dir + name
        return self.current_dir + '/' + name

    def _normalize_path(self, path_name: str) -> str:
        if path_name != "/" and path_name.endswith('/'):
            path_name = path_name.rstrip('/')
        return path_name

    def make_dir(self, dir_name: str) -> bool:
        abs_path = self._join_path(dir_name)
        if (abs_path, 'f') in self.file_system[self.current_dir] or (abs_path, 'd') in self.file_system[self.current_dir]:
            return False
        else:
            self.file_system[self.current_dir].append((abs_path, 'd'))
            self.file_system[abs_path] = []
            return True

    def create_file(self, file_name: str) -> bool:
        abs_path = self._join_path(file_name)
        if (abs_path, 'f') in self.file_system[self.current_dir] or (abs_path, 'd') in self.file_system[self.current_dir]:
            return False
        else:
            self.file_system[self.current_dir].append((abs_path, 'f'))
            return True

    def change_dir(self, path_name: str) -> bool:
        if path_name == "":
            return True
        path_name = self._normalize_path(path_name)
        if not path_name.startswith('/'):
            path_name = self.current_dir + path_name if self.current_dir.endswith('/') else self.current_dir + '/' +path_name

        if path_name in self.file_system:
            self.current_dir = path_name
            return True
        return False
       

    def remove(self, name: str) -> bool: 
        abs_path = self._join_path(name)
        if (abs_path, 'f') in self.file_system[self.current_dir]:
            self.file_system[self.current_dir].remove((abs_path, 'f'))
            return True
        elif (abs_path, 'd') in self.file_system[self.current_dir]:
            prefix = abs_path + '/'
            delete_paths = [path for path in self.file_system if path == abs_path or path.startswith(prefix)]
            for path in delete_paths:
                del self.file_system[path]
            self.file_system[self.current_dir].remove((abs_path, 'd'))
            return True
        else:
            return False

    def list_dir(self) -> List[str]:
        res = []
        content = self.file_system[self.current_dir]
        sorted_content = sorted(content, key=lambda x : (x[1], x[0]))
        for c in sorted_content:
            res.append(c[0].split('/')[-1])


        return res


def run_sample_1() -> None:
    fs = FileSystem()
    print("null")
    print(fs.make_dir("dirc"))
    print(fs.make_dir("dirb"))
    print(fs.make_dir("dirc"))
    print(fs.list_dir())
    print(fs.change_dir("dirc/"))
    print(fs.create_file("fileb"))
    print(fs.make_dir("dirb"))
    print(fs.create_file("dirb"))
    print(fs.list_dir())
    print(fs.change_dir("/dirb/dirc"))


def run_sample_2() -> None:
    fs = FileSystem()
    print("null")
    print(fs.list_dir())
    print(fs.change_dir(""))
    print(fs.create_file("gateway"))
    print(fs.make_dir("home"))
    print(fs.change_dir("gateway"))
    print(fs.make_dir("etc"))
    print(fs.list_dir())
    print(fs.remove("gateway"))
    print(fs.change_dir("etc/"))
    print(fs.create_file("pip"))
    print(fs.change_dir("/etc/"))
    print(fs.list_dir())
    print(fs.change_dir("/"))
    print(fs.remove("etc"))
    print(fs.list_dir())


if __name__ == "__main__":
    print("sample 1")
    run_sample_1()
    print()
    print("sample 2")
    run_sample_2()
