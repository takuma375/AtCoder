N = int(input())
S = input()

list = []

for i in range(N):
    if S[i] == "1":
        list.append(i)

if list[0] % 2 == 0:
    print("Takahashi")
else:
    print("Aoki")
