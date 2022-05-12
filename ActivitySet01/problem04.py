# Conditional Execution

hrs = float(input("Enter hours?"))
rph = float(input("enter rate"))
if(hrs<=40):
  gp= rph*hrs
  print("gross pay is",gp)
elif(hrs>40):
  gp=((rph*40)+(1.5*rph*(hrs-40)))
  print("gross pay",gp)

