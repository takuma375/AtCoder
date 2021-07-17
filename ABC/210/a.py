N, A, X, Y = list(map(int, input().split()))

sum = 0

for i in range(1, N+1):
    if i<=A:
        sum += X
    else:
        sum += Y

print(sum)
