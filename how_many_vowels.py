def vowels(w):
  x=0
  for char in w:
    if char in "a":
      x+=1
  for char in w:
    if char in "e":
      x+=1
  for char in w:
    if char in "i":
      x+=1
  for char in w:
    if char in "o":
      x+=1
  for char in w:
    if char in "u":
      x+=1
  print(x)
vowels("vowel test")
