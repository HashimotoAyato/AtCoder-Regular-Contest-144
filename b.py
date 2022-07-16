import numpy as np

N, a, b = map(int, input().split())
A = list(map(int, input().split()))

A.sort()

while b - a < A[-1] - A[0]:
    A[0] += a
    A[-1] -= b
    A.sort()

print(A[0])