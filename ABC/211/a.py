a, b = list(map(int, input().split()))

if (a-b) %3 == 0:
    print((a-b) // 3 + b)
else:
    print((a-b) / 3 + b)