import math


def prob(n, p, N):
    C = math.factorial(N) / (math.factorial(n) * math.factorial(N - n))
    return C * (p ** n) * ((1 - p) ** (N - n))


def infoMeasure(n, p, N):
    return -math.log2(prob(n, p, N))


def sumProb(N, p):
    '''
    Giả sử với p = 0.5, ta thử với các giá trị của N:
      N = 5 => sumProb(5, 0.5) = 1
      N = 10 => sumProb(10, 0,5) = 1
      N = 15 => sumProb(15, 0.5) = 1
      N = 20 => sumProb(20, 0.5) = 1
    Ta thấy với mọi N thì sumProb(N, 0.5) = 1
    Suy ra hàm sumProb có thể sử dụng để kiểm chứng tổng xác suất của phân bố binomial bằng 1.
    '''
    result = 0
    for i in range(0, N + 1):
        result += prob(i, p, N)
    return result


def approxEntropy(N, p):
    result = 0
    for i in range(0, N + 1):
        result += prob(i, p, N) * infoMeasure(i, p, N)
    return result
