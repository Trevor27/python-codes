# this program uses nested loops to create a number pyramid

# all numbers in range are represented by variable (i)

for i in range (1,10):
    output = str(i)

# all numbers in range are represented by variable (c) and merged with the above loop
    for c in range (2,i+1):
        val = i * c
        output += "\t"+str(val)
    print(output)
