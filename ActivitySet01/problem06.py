# Loops & Iterators
largest = 0
smallest = 0
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    elif(num.isdecimal()==True):
        largest=max(int(num),largest)
        
        print(num)
    elif(num.isalpha()==True):
        print("invalid input")
    
    
print("Maximum", largest)
print("Minimum",smallest)

