def ans(x,y,d,visit,count=0):
  if(x,y) in visit:
    return False,count
  visit.add((x,y))
  count+=1
  print(f"State: ({x}, {y})")

  if x==d or y==d:
    return True,count

  if x<0 or y<0 or x>m or y>n:
    return False,count

  #fill 1
  result,count=ans(m,y,d,visit,count)

  if result:
    return True,count

  #fill 2
  result,count=ans(x,n,d,visit,count)
  if result:
    return True,count

  #empty 1:
  result,count=ans(0,y,d,visit,count)
  if result:
    return True,count

  #empty 2:
  result,count=ans(x,0,d,visit,count)
  if result:
    return True,count

  #pour 1->2
  amt=min(x,n-y)
  result,count=ans(x-amt,y+amt,d,visit,count)
  if result:
    return True,count

  #pour 2->1
  amt=min(y,m-x)
  result,count=ans(x+amt,y-amt,d,visit,count)
  if result:
    return True,count

  return False,count


m,n=map(int,input().split())
d=int(input("desired limit for jug2:"))
visit=set()
if abs(m-n)>1:
  print("invalid")
else:
  result,count=ans(0,0,d,visit)
  print(count)