def calc(n1,o,n2):
  if o == "+":
    return(n1+n2)
    
  if o == "-":
    return(n1-n2)
    
  if o == "*":
    return(n1*n2)
    
  if o == "/":
    if n2==0:
      return("Cant divide by 0!")
    else:
      return(n1/n2)
      

printCalc=calc(0,"/",0)
print(printCalc)
