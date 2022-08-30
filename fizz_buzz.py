def fb(n):
  if n%3==0 and n%5==0:
    print("Fizz Buzz")
  elif n%3==0:
    print("Fizz")
  elif n%5==0:
    print("Buzz")
  else:
    print(n)
fb(3)
fb(5)
fb(15)
fb(4)
