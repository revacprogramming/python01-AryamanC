# Loops & Iterators
largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if(num>largest):
        largest=num
    if(smallest>num):
        smallest=num
    if num == "done":
        break
    else:
        print("invalid input")
        continue
    print(num)
    
print("Maximum", largest)
print("Minimum",smallest)
