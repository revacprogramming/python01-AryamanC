# Functions
def computepay(h, r):
    if(h<=40):
        gp=h*r
    elif(h>40):
        gp=((r*40)+(1.5*r*(h-40)))
    return gp

hrs = float(input("Enter Hours:"))
rph = float(input("enter rate per hour"))
p = computepay(hrs,rph)
print("Pay", p)


