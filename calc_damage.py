def damage(d,s,t):
  if t == "second" and d>0 and s>0:
    print(d*s*1)
  elif t == "minute" and d>0 and s>0:
    print(d*s*60)
  elif t == "hour" and d>0 and s>0:
    print(d*s*3600)
  elif t == "day" and d>0 and s>0:
    print(d*s*86400)
  else:
    print("Invalid")

damage(45,1,"day")
