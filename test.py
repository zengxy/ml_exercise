#test file
__author__ = 'zxy'

class myclass():
    def __init__(self):
        self.num=1



if __name__ == '__main__':
    a=myclass()
    print(a.num)
    a.num=2

    b=myclass()
    print(myclass.__dict__)
    print(b.num)