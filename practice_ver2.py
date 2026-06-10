#3
#Python 2
#英語 1
#数学 3
#このように入力すると今どれだけ学習したかを記録できるプログラムです
#合計 6時間
N=int(input())
goukei=0
max_gakusyuu=0
gakusyuu = {}

for i in range(N):
    kyouka, jikan = input().split()
    jikan = int(jikan)
    if kyouka in gakusyuu:
      gakusyuu[kyouka]+=jikan
    else:
      gakusyuu[kyouka] = jikan

for x in gakusyuu:
    gakusyuu[x]=int(gakusyuu[x])
    goukei+=gakusyuu[x]
    if max_gakusyuu <= gakusyuu[x]:
      max_gakusyuu=gakusyuu[x]
      max_kyouka=x
print("勉強時間:",goukei,"時間")
print("最も学習した科目:",max_kyouka)