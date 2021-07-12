# n個の整数 ai(i=1,2,...n)を入力し、それらの最小値、最大値、合計値を求めるプログラムを作成してください。
# １行目に整数の数 nが与えられます。２行目に n個の整数 aiが空白区切りで与えられます。

n = int(input())
nList = list(map(int, input().split()))

min = min(nList)
max = max(nList)
sum = sum(nList)

print(min, max, sum)
