import math


def prob(n, p):
    return p * ((1 - p) ** (n - 1))


def infoMeasure(n, p):
    return -math.log2(prob(n, p))


def sumProb(N, p):
    '''
    Giả sử với p = 0.5, ta thử với các giá trị của N:
      N = 4 => sumProb(4, 0.5) = 0.9375
      N = 8 => sumProb(8, 0,5) = 0.9961
      N = 12 => sumProb(12, 0.5) = 0.9998
      N = 16 => sumProb(16, 0.5) = 0.9999
      Với N càng lớn thì sumProb càng tiến dần đến 1
    Suy ra hàm sumProb có thể sử dụng để kiểm chứng tổng xác suất của phân bố geometric bằng 1. 
    '''
    result = 0
    for i in range(1, N + 1):
        result += prob(i, p)
    return result


def approxEntropy(N, p):
    '''
    Ta có entropy của nguồn geometric với giá trị p = 0.5 bằng 2.
    Giả sử với p = 0.5, ta thử với các giá trị của N:
      N = 5 => approxEntropy(5, 0.5) = 1.7813
      N = 10 => approxEntropy(10, 0.5) = 1.9883
      N = 15 => approxEntropy(15, 0.5) = 1.9995
      N = 20 => approxEntropy(20, 0.5) = 1.9999
      Với N càng lớn thì approxEntropy càng tiến dần đến 2
    Suy ra hàm approxEntropy tính xấp xỉ entropy của nguồn tin geometric
    '''
    result = 0
    for i in range(1, N + 1):
        result += prob(i, p) * infoMeasure(i, p)
    return result
