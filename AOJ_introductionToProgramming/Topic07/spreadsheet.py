# 行数r, 列数c
r, c = list(map(int, input().split()))

# データを保管するための2次元配列を定義
sheet = [[0 for i in range(c+1)] for j in range(r+1)]

# 標準入力からデータを受け取り、sheetに格納する。
for i in range(r):
    row = list(map(int, input().split()))
    for j, value in enumerate(row):
        sheet[i][j] = value

# 行の和を計算し、sheetに格納する
for i, row in enumerate(sheet):
    sum_row = 0
    for j, value in enumerate(row):
        sum_row += value
    sheet[i][j] = sum_row

# 列の和を計算し、sheetに格納する
for i in range(c+1):
    sum_culumn = 0
    for j in range(r):
        sum_culumn += sheet[j][i]
    sheet[j+1][i] = sum_culumn

for i, row in enumerate(sheet):
    for j, value in enumerate(row):
        if j == c:
            print(value)
        else:
            print(f"{value} ", end="")

