# 筛法求1~n的素数
from math import sqrt


def SieyeForPrimeNum(n):
    Nums = [x for x in range(3, n + 1, 2)]
    restNum = Nums.__len__()
    maxSieve = int(sqrt(n))
    sieve = 3
    cycle = 0
    sieve = Nums[cycle]
    while sieve <= maxSieve:
        count = 0
        for i in range(cycle + 1, restNum - 1):
            if Nums[i] % sieve == 0:
                count += 1
            else:
                Nums[i - count] = Nums[i]
        restNum -= count
        cycle += 1
        sieve = Nums[cycle]
    for i in range(0, restNum - 1):
        print(Nums[i])


if __name__ == '__main__':
    SieyeForPrimeNum(10000000)