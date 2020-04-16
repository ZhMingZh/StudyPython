import os
import time

files_list = []


def log(func):

    def wrapper(*args, **kwargs):
        start = time.time()
        midea = func(*args, **kwargs)
        print('函数耗时：{}'.format(time.time() - start))
        return midea

    return wrapper


def find_file(dirpath, ext):

    for path in os.listdir(dirpath):
        abspath = os.path.join(dirpath, path)
        if os.path.isdir(abspath):
            find_file(abspath, ext)
        elif os.path.splitext(path)[1] == ext:
            files_list.append(os.path.join(dirpath, path))

@log
def get_file(dir, ext):
    all_files = []
    for root, dirs, files in os.walk(dir):
        for file in files:
            abspath = os.path.join(root, file)
            if os.path.splitext(file)[1] == ext:
                all_files.append(abspath)
    return all_files


if __name__ == '__main__':

    start = time.clock()
    find_file('/Users/skydream/PycharmProjects/StudyPython', '.py')
    print('函数耗时：{}'.format(time.clock() - start))

    # print("递归查找", dict(Counter(list)))
    all_files = get_file('/Users/skydream/PycharmProjects/StudyPython', '.py')

    print(len(files_list), len(all_files))
    # print("os.walk查找", dict(Counter(all_files)))

    print(set(files_list) - set(all_files))
    # print(files_list)
    # print(len(set(all_files)))
