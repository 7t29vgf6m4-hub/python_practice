#上から順番に（行が）人となっていて列が教科別でそのテストの点数が入力です。
#N人も入力します。
# 80, 70, 90
# 60, 50, 70
# 100, 90, 80
#]
#について

#各行の合計
#各行の平均

#（出力）を求めるプログラムを書く。
N=int(input())
A = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
   goukei=sum(A[i])
   average=goukei/3
   print(goukei,average)