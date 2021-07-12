# 半径 r の円の面積と円周の長さを求めるプログラムを作成して下さい。

r = float(input())

pie = float(3.141592653589)

sqare = pie * r * r
circumference = 2 * pie * r

# print(sqare, circumference)
print(f"{sqare:.6f} {circumference:.6f}")