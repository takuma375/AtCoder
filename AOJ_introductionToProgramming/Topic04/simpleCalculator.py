# ２つの整数 a, b と１つの演算子 op を読み込んで、a op b を計算するプログラムを作成して下さい。
# ただし、演算子 op は、"+"(和)、"-"(差)、"*"(積)、"/"(商)、のみとし、
# 割り算で割り切れない場合は、小数点以下を切り捨てたものを計算結果とします。

while True:
    a, op, b = input().split()
    a = int(a)
    b = int(b)
    if op == "+":
        print(a+b)
    elif op == "-":
        print(a-b)
    elif op == "*":
        print(a*b)
    elif op == "/" and b != 0:
        print(a/b)
    elif op == "?":
        break
