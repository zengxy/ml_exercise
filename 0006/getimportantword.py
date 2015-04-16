# 你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词。
__author__ = 'zengxianyu'


def countMost(file):
    word_dict = {}
    with open(file) as f:
        for line in f:
            words = line.split()
            for word in words:
                if word in word_dict:
                    word_dict[word] += 1
                else:
                    word_dict[word] = 1
        word_dict = {word_dict[key]: key for key in word_dict}
        return (word_dict[max(word_dict)], max(word_dict))

        pass


if __name__ == '__main__':
    word, num = countMost('test.txt')
    print(word, num)