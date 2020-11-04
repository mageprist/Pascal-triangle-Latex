import math
n = 10

print ('\\begin{tabular}{%s}' % ('c' * (2*n)))

for x in range(n):
    string = ""

    string += " &" * (n-x -1)
    
    for y in range(x+1):
        if y == 0:
            string += str(math.comb(x, y))
        else:
            string += "& &" + str(math.comb(x, y))
    string += "\\" + "\\"
    print(string)
print("\end{tabular}")
