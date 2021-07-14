# 与えられた数列を逆順に出力するプログラムを作成して下さい。

n = int(input())
A = list(map(int, input().split()))

A.reverse()

for i, a in enumerate(A):
    if i > 0:
        print(" ", end="")
    print(a, end="")
print()
