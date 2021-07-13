N, X = list(map(int, input().split()))
prices = list(map(int, input().split()))

sum = 0

for i in range (N):
    if i%2 == 0:
        sum += prices[i]
    else:
        sum += prices[i] - 1

if X >= sum:
    print("Yes")
else:
    print("No")