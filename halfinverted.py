# Half Inverted Pyramid Pattern

rows = 6

for i in range (rows, 0, -1):
    for j in range(0, i):
        print(j, end="")
    print()
    
# Output:
# 012345
# 01234
# 0123
# 012
# 01
# 0