# 秒単位の時間 Sが与えられるので、h:m:sの形式へ変換して出力してください。
# ここで、hは時間、mは 60 未満の分、sは 60 未満の秒とします。

S = int(input())

hours = int(S / 3600)
minutes = int(S%3600/60)
seconds = int(S%3600%60)

print(f"{hours}:{minutes}:{seconds}")