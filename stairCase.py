#First I have the entarance of the number of rows required
n = int(input("Enter with a value: "))

def piram(v):
    value = v
    for i in range(1, value + 1):
        for j in range(1, i + 1):
            print("#", end=""),
        print()
#this is another way to do it. I'd rather this below;
#for i in range(1, n + 1):
#        print(str('#'*i).rjust(n, ' '))

piram(n)
