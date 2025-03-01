# Reverse Pyramid Pattern

rows = 5

for i in range (1, rows +1):
    for j in range(i, 0, -1):
        print(j, end="")
    print()

# Output:
# 1
# 21
# 321
# 4321
# 54321