# Full Pyramid 

rows = 9

for i in range(1, rows + 1):
    for j in range(rows - i):
        print(' ', end='')
        
    for k in range(0, i):
        print(i, end=' ')
    print()
    
# Output:
#         1
#        2 2
#       3 3 3
#      4 4 4 4
#     5 5 5 5 5
#    6 6 6 6 6 6
#   7 7 7 7 7 7 7
#  8 8 8 8 8 8 8 8
# 9 9 9 9 9 9 9 9 9