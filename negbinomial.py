import math


def prob(n, p, r):
    C = math.factorial(n - 1) / (math.factorial(r - 1) * math.factorial(n - r))
    return C * (p ** r) * ((1 - p) ** (n - r))


def infoMeasure(n, p, r):
    return -math.log2(prob(n, p, r))


def sumProb(N, p, r):
    '''
    Giả sử với p = 0.5, r = 5 ta thử với các giá trị của N:
      N = 10 => sumProb(10, 0.5, 5) = 0.6230
      N = 20 => sumProb(20, 0.5, 5) = 0.9941
      N = 40 => sumProb(40, 0.5, 5) = 0.9999
      Với N càng lớn thì sumProb càng tiến dần đến 1
    Suy ra hàm sumProb có thể sử dụng để kiểm chứng tổng xác suất của phân bố negbinomial bằng 1.
    '''
    result = 0
    for i in range(r, N + 1):
        result += prob(i, p, r)
    return result


def approxEntropy(N, p, r):
    '''
    Ta có entropy của nguồn negbinomial với giá trị p = 0.5, r = 6 xấp xỉ 3.7384.
    Giả sử với p = 0.5, r = 6 ta thử với các giá trị của N:
      N = 15 => approxEntropy(15, 0.5, 6) = 2.9054
      N = 30 => approxEntropy(30, 0.5, 6) = 3.7360
      N = 50 => approxEntropy(50, 0.5, 6) = 3.7384
      Với N càng lớn thì approxEntropy càng tiến dần đến 3.7384
    Suy ra hàm approxEntropy tính xấp xỉ entropy của nguồn tin negbinomial
    '''
    result = 0
    for i in range(r, N + 1):
        result += prob(i, p, r) * infoMeasure(i, p, r)
    return result
