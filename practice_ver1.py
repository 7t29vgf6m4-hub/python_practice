#3
#Python 2
#英語 1
#数学 3
#このように入力すると今どれだけ学習したかを記録できるプログラムです
#合計 6時間
N=int(input())
gakusyuu=[list(input().split()) for _ in range(N)] 
goukei=0
max_gakusyuu=0

for i in range(N):
   gakusyuu[i][1]=int(gakusyuu[i][1])
   goukei+=gakusyuu[i][1]
   if max_gakusyuu <= gakusyuu[i][1]:
      max_gakusyuu=gakusyuu[i][1]
      max_kyouka=gakusyuu[i][0]
print("勉強時間:",goukei,"時間")
print("最も長く学習した科目:",max_kyouka)