# Strings

text = "X-DSPAM-Confidence:    0.8475"
a=len(text)
n=""
for i in range(0,a-1):
    if(text[i].isdecimal()==True):
        n=n+text[i:a]
        break
num1=float(n)
print(num1)