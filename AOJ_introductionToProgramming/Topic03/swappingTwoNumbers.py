# ２つの整数 x, y を読み込み、それらを値が小さい順に出力するプログラムを作成して下さい。
# 入力は複数のデータセットから構成されています。各データセットは空白で区切られた２つの整数 x, y を含む１行から構成されています。
# x と y がともに 0 のとき入力の終わりを示し、このデータセットに対する出力を行ってはいけません。

while True:
    x, y = list(map(int, input().split()))
    if x == 0 and y == 0:
        break
    elif x > y:
        x, y = y, x
    print(x, y)