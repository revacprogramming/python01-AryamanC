# Files
fname = input("Enter file name: ")
fh = open(fname)
count = 0
x = 0

for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        count = count + 1
        z = line.find(':')
        y = float(line[z+1:])
        x = float(x + y)

asc = x / count
print("Average spam confidence:",asc)
