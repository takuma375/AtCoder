# たて a cm よこ b cm の長方形の面積と周の長さを求めるプログラムを作成して下さい。
l = input()
a, b = list(map(int,l.split()))

# 面積
square = a * b
# 周長
perimiter = (a + b)*2

print(square, perimiter)
