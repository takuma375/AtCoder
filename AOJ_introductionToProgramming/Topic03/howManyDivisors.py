# ３つの整数a、b、cを読み込み、aからbまでの整数の中に、cの約数がいくつあるかを求めるプログラムを作成してください。

a, b, c = list(map(int, input().split()))

count = 0
i = 1

while i <= c:
    if (c % i == 0) and (a <= i <= b):
        count += 1
    i += 1

print(count)