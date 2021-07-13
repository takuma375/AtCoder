# A以上かつ B以下の整数はいくつありますか？

A, B = list(map(int, input().split()))

count = 0

for i in range(A, B+1):
    if A > B:
        count = 0
        break
    else:
        count += 1

print(count)