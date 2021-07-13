# １つの整数 n が１行に与えられます。
# 上記プログラムに入力の整数 nを与えた結果を出力してください。

n = int(input())
x = 0

for i in range(1, n+1):
    if i%3 == 0:
        print("", i, end="")
    else:
        x = i
        while x:
            if x%10 == 3:
                print("", i, end="")
                break
            x //= 10
print()