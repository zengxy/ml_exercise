# 有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来
__author__ = 'zengxianyu'

import sys

def countLines(filepath):
    total_lines = 0
    empty_lines = 0
    comment_lines = 0
    with open(filepath,encoding=sys.getdefaultencoding()) as f:
        for line in f:
            total_lines += 1
            if line.strip() == '':
                empty_lines += 1
            elif line.strip().startswith("#"):
                comment_lines += 1
        f.close()
        return total_lines, empty_lines, comment_lines
    return 0, 0, 0


if __name__ == '__main__':
    file = 'a.txt'
    print(countLines(file))