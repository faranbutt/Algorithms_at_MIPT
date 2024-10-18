# This is a template for problem Sigma-Trimpazation.

from time import time

# set the following flag to True to estimate execution time
#
# Exact execution time on you device may be different
# from one on Yandex contest platform!
#
# The flag MUST be False when you are submitting your solution!
estimate_execution_time = False

# Fixed parameters of quantum process:
quantum_a = 7**5
quantum_m = 2**31 - 1

# def counting_sort(arr):
#     min_val = min(arr)
#     max_val = max(arr)
#     shift = -min_val
#     M = max_val + shift + 1
#     a = [0] * M
#     for i in arr:
#         a[i+shift] += 1
#     for i in range(1,M):
#         a[i] += a[i-1]
#     res = [None] * N
#     for i in range(N):
#         position = a[arr[i]+shift] - 1
#         res[position] = arr[i]
#         a[arr[i]+shift] -= 1
#     return res


def analyze_trimpazation(n, m, q0):
    '''
    This function generates data with given parameters
    and calculates desired Y value.

    You need to modify it to make it execute faster.
    You can check your progress using estimate_execution_time flag
    at the top of the file.
    '''
    m_div2 = m // 2
    q = q0
    # generating x data:
    x = []
    count = [0] * m
    shift = m_div2
    for i in range(n):
        x_i = q % m - m_div2
        count[x_i+shift] += 1
        q = ((q * quantum_a) % quantum_m)
    # sorting x data:

    # calculating sum:
    res = 0
    index = 0
    for i in range(-m_div2,m - m_div2):
        count_value = count[i + shift]
        if count_value > 0:
            for j in range(count_value):
                index += 1
                res += index * i

    return res


if __name__ == '__main__':
    N, M, q0 = map(int, input().split())
    t = time()
    print(analyze_trimpazation(N, M, q0))
    if estimate_execution_time:
        print(f'Execution time = {time() - t:.8f} seconds')


