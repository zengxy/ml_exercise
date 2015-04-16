# 任一个英文的纯文本文件，统计其中的单词出现的个数。不同的
__author__ = 'zengxianyu'

symbols = ''' ~`!@#$%^&*()-_=+{}[]|\:";""'',./<>? '''


def countword(filepath, mark=symbols):
    wordic = set()
    with open(filepath) as f:
        for line in f:
            words = line.split()
            for word in words:
                if mark.find(word) == -1:
                    wordic.add(word)
    f.close()
    print(wordic)


if __name__ == '__main__':
    countword("test.txt")