#       *       * 
#       * *   * * 
#       * * * * * 
#       * *   * * 
#       *       * 




num=7
for row in range(num):
    for col in range(num):
        if col==0 or row+col==num-1 or col==num-1 or row==col or row ==num//2:
            print('*', end=' ')
        else:
            print(' ',end=' ')    
    print()        