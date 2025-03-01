# Inverted Pyramid of Same Numbers

rows = 5

num = rows

for i in range (rows, 0, -1):
    for j in range (0, i):
        print(num, end="")
    print()
    
# Output:
# 55555
# 5555
# 555
# 55
# 5