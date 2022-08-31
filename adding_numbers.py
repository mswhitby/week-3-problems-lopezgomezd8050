#old code
def add(n1,n2):
  return n1+n2
n3=add(1,6)
print(n3)

#new better code

def add(n1,n2):
  if (n1 != "" or None) and (n2 != "" or None):
    n3=(int(n1)+int(n2))
    print(str(n3))
  else:
    print("invalid operation")
add("6","3")
