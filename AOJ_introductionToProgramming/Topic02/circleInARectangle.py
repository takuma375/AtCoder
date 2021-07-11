# ５つの整数 W、H、x、y、rが空白区切りで１行に与えられます。
# 円が長方形の内部に含まれるなら Yes と、一部でもはみ出るならば No と１行に出力してください。

w, h, x, y, r = list(map(int, input().split()))

if 0 <= (x-r) and 0 <= (y-r) and (x+r) <= w and (y+r) <= h:
    print("Yes")
else:
    print("No")