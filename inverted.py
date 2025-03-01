# Inverted Pyramid

rows = 5

for i in range (1, rows + 1):
    for j in range(rows - i + 1):
        print(i, end="")
    print()    
    
#Output
# 11111
# 2222
# 333
# 44
# 5