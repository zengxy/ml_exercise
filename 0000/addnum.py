# 将你的QQ头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果
__author__ = 'zengxianyu'
from PIL import Image, ImageDraw, ImageFont


def addNum(filepath, text):
    im = Image.open(filepath)
    x, y = im.size
    text = str(text)

    fnotsize = int(min(x, y) / (text.__len__() * 2))
    print(fnotsize)
    textlen = fnotsize * text.__len__()

    fnt = ImageFont.truetype("/Library/Fonts/华文仿宋.ttf", fnotsize)
    ImageDraw.Draw(im).text((x - textlen / 2, 0), str(text), font=fnt, fill="red")
    im.show()


if __name__ == '__main__':
    addNum("1.png", "10")