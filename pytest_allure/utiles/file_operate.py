import os
import shutil
import hashlib


# 查找文件夹中的某个文件
def find_file_dir(dir_path, find_file):
    files = []
    dirs = []
    for root, dirs, files in os.walk(dir_path, topdown=False):
        for file in files:
            if file == find_file:
                return root
        for dir in dirs:
            find_file_dir(os.path.join(root, dir), find_file)


# 创建文件夹
def make_dirs(dir_path):
    os.makedirs(dir_path, exist_ok=True)


# 删除文件
def del_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)


# 删除文件夹里所有的文件
def del_dir(dir_path):
    if os.path.isdir(dir_path):
        for f in os.listdir(dir_path):
            del_dir(os.path.join(dir_path, f))
        if os.path.exists(dir_path):
            os.rmdir(dir_path)
    else:
        if os.path.exists(dir_path):
            os.remove(dir_path)


# 拷贝文件
def copy_file(source_file_path, dest_file_path):
    if not (os.path.exists(source_file_path)):
        return False

    if os.path.exists(dest_file_path):
        if get_file_md5(source_file_path) == get_file_md5(dest_file_path):
            return True
        else:
            os.remove(dest_file_path)

    dest_file_dir = os.path.dirname(dest_file_path)
    os.makedirs(dest_file_dir, exist_ok=True)
    if not (shutil.copyfile(source_file_path, dest_file_path, follow_symlinks=False)):
        return False
    return True


# 拷贝文件夹里的文件
def copy_dir(source_dir, dest_dir):
    if not (os.path.exists(source_dir)):
        return False

    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)

    if not (shutil.copytree(source_dir, dest_dir, symlinks=True)):
        return False
    return True


# 获取文件的md5
def get_file_md5(file_path):
    with open(file_path, 'rb') as f:
        content = f.read()
    hash = hashlib.md5()
    hash.update(content)
    return hash.hexdigest()


# 获取一个文件夹里的所有的文件和该文件对应的md5
def dir_list(dir_path):
    list_dict = {}
    files = []
    dirs = []
    for root, dirs, files in os.walk(dir_path, topdown=False, followlinks=True):
        for file in files:
            file_path = os.path.join(root, file)
            list_dict[os.path.relpath(file_path, dir_path).replace(
                '\\', '/')] = get_file_md5(file_path)
    for dir in dirs:
        dir_list(os.path.join(root, dir))
    return list_dict


# 逐行读一个文件，并过来文件中某些行里回车和空格
def read_line_for_file(file_path):
    f = open(file_path, 'r')
    lines = f.readlines()
    f.close()
    new_lines = []
    for line in lines:
        line = line.replace('\n', '').strip()
        if line:
            new_lines.append(line)
    return new_lines
