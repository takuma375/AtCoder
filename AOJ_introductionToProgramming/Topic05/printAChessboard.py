# たてH cm よこ W cm のチェック柄の長方形を描くプログラムを作成して下さい。
# 入力は複数のデータセットから構成されています。各データセットの形式は以下のとおりです：H W
# H, W がともに 0 のとき、入力の終わりとします。

# while True:
#     H, W = list(map(int, input().split()))
#     if H == 0 and W == 0:
#         break
#     else:
#         for i in range(H):
#             for j in range(W):
#                 if i%2 == 0:
#                     if j%2==0:
#                         print("#", end="")
#                     else:
#                         print(".", end="")
#                 else:
#                     if j%2 == 0:
#                         print(".", end="")
#                     else:
#                         print("#", end="")
#             print()
#         print()

while True:
    H, W = list(map(int, input().split()))
    if H == 0 and W == 0:
        break
    else:
        for i in range(H):
            for j in range(W):
                if (i+j) % 2 == 0:
                    print("#", end="")
                else:
                    print(".", end="")
            print()
        print()