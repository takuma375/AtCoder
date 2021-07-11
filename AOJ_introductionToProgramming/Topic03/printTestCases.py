# 入力は複数のデータセットから構成されています。各データセットは１つの整数 x を含む１行から構成されています。
# xが0のとき入力の終わりを示し、このデータセットに対する出力を行ってはいけません。

count = 1
while True:
    x = int(input())
    if x == 0:
        break
    print(f"Case {count}: {x}")
    count += 1