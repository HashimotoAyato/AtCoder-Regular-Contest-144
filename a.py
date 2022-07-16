N = int(input())

# 最大のMを求める。
x = []
n = N
while n > 4:
    n -= 4
    x.append(4)
x.append(n)
M = 0
for i in range(len(x)):
    M += x[i] * 2

print(M)

# 最小のxを求める。
x = []
n = N
if n%4 > 0:
    x.append(n%4)
    n -= n%4
while n > 0:
    n -= 4
    x.append(4)

for i in range(len(x)):
    print(x[i], end='')
print()