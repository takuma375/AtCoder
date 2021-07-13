N = int(input())
C = list(map(int, input().split()))
C.sort()

count = 1

for i in range(N):
    count = count * max(0, C[i] - i) % 1000000007

print(count)