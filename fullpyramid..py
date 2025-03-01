# Full Pyramid 

rows = 9

for i in range(1, rows + 1):
    for j in range(rows - i):
        print(' ', end='')
        
    for k in range(0, i):
        print(i, end=' ')
    print()
    
