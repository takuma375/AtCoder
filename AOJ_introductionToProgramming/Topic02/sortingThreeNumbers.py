# ３つの整数を読み込み、それらを値が小さい順に並べて出力するプログラムを作成して下さい。

a, b, c = list(map(int, input().split()))

if a > b:
    tmp = a
    a = b
    b = tmp

if b > c:
    tmp = b
    b = c
    c = tmp

if a > b:
    tmp = a
    a = b
    b = tmp

print(a, b, c)