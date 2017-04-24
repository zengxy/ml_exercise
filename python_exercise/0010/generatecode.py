# 使用 Python 生成类似于下图中的**字母验证码图片**
__author__ = 'zxy'

import random
import string
from PIL import Image, ImageDraw, ImageFont

fontPath = 'arial.ttf'


def generateCode(canditateSet, len=5):
    code = ' '.join([random.choice(canditateSet) for i in range(len)])
    return code


def generateIMG(str, charsize=20):
    im = Image.new(mode='RGB', size=(int (charsize * str.__len__()/2), charsize), color=(0, 240, 240))
    font = ImageFont.truetype(fontPath, charsize)
    ImageDraw.Draw(im).text((0, 0), str, 'red', font)
    im.show()
    im.save("text.png")


if __name__ == '__main__':
    code = generateCode(string.ascii_letters + string.digits)
    generateIMG(code)
                                                                                                                                                                                                                                                              