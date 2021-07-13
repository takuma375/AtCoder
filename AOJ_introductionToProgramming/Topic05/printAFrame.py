# たてH cm よこ W cm の枠を描くプログラムを作成して下さい。

# 入力は複数のデータセットから構成されています。各データセットの形式は以下のとおりです：
# H W
# H, W がともに 0 のとき、入力の終わりとします。

while True:
    H, W = list(map(int, input().split()))

    if H == 0 and W == 0:
        break
    else:
        for i in range(H):
            for j in range(W):
                if i == 0 or i == (H - 1):
                    print("#", end="")
                elif j == 0 or j == (W-1):
                    print("#", end="")
                else:
                    print(".", end="")
            print()
        print()