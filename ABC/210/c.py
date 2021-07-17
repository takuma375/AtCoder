N, K = list(map(int, input().split()))
C = list(map(int, input().split()))

current = 0
candy_map = {}

for i in range(N):
    candy_map.setdefault(C[i], 0)

for i in range(K):
    if candy_map[C[i]] == 0:
        current += 1
    candy_map[C[i]] += 1

answer = current
for i in range(N-K):
    if candy_map[C[i]] == 1:
        current -= 1
    candy_map[C[i]] -= 1

    if candy_map[C[i+K]] == 0:
        current += 1
    candy_map[C[i+K]] += 1
    answer = max(answer, current)

print(answer)
