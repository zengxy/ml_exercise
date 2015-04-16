# 你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。
__author__ = 'zengxianyu'

from PIL import Image
import os

iphone5Size = (30, 100)
baseDir = './'


def resizeImage(imageName, imagePath=baseDir, targetSize=iphone5Size):
    try:
        im = Image.open(imagePath + imageName)
        name, extension = imageName.split('.')
        targetX, targetY = targetSize
        x, y = im.size
        x = min(x, targetX)
        y = min(y, targetY)

        print(x, y)
        out = im.resize((x, y))
        out.save(imagePath + name + '_resize.' + extension)
    except:
        pass


if __name__ == '__main__':
    for root, dirs, files in os.walk(baseDir):
        for image in files:
            resizeImage(image, root)