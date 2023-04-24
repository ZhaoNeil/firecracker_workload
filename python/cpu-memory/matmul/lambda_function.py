import numpy as np
from time import time
import sys


def matmul(n):
    A = np.random.rand(n, n)
    B = np.random.rand(n, n)

    start = time()
    C = np.matmul(A, B)
    latency = time() - start
    return latency

if __name__ == "__main__":
    n = int(sys.argv[1])
    result = matmul(n)
    print(result)
