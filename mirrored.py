# Mirrored Pyramid

rows = 6

for i in range (1, rows):
    for j in range(rows-i):
        print(" ", end="")
    for k in range(i):
        print(i, end="")
    print()
    
# Output:
#      1
#     22
#    333
#   4444
#  55555