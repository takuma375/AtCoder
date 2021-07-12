# ２つの整数 a と b を読み込んで、以下の値を計算するプログラムを作成して下さい：
# a ÷ b ： d (整数)
# a ÷ b の余り ： r (整数)
# a ÷ b ： f (浮動小数点数)

a, b = list(map(int, input().split()))

d = a // b
r = a % b
f = a / b

print(d, r, f"{f:.5f}")