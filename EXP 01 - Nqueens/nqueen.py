N=int(input("enter number of queens:"))
board=[[0]*N for _ in range(N)]
def attack(i,j):
  for k in range(0,N):
    if board[i][k]==1 or board[k][j]==1:
      return True

  for k in range(0,N):
    for l in range(0,N):
      if (k+l==i+j) or (k-l==i-j):
        if board[k][l]==1:
          return True
  return False


def ans(n):
  if n==0:
    return True
  for i in range(0,N):
    for j in range(0,N):
      if (not(attack(i,j))) and (board[i][j]!=1):
        board[i][j]=1
        if ans(n-1)==True:
          return True
        board[i][j]=0
  return False


if ans(N) == False:
    print("does not exist")
else:
    for i in board:
        print(i)