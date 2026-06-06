N, M = map(int, input().split())
AB = [list(map(int, input().split())) for i in range(M)]
game=[["-"] * N for _ in range(N)]

for i in range(M):
  game[AB[i][0]-1][AB[i][1]-1]="o"
  game[AB[i][1]-1][AB[i][0]-1]="x"
  
for i in range(N):
  print(*game[i])