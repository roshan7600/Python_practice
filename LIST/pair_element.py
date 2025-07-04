L=[0,1,2,3,4,5,6,7]
target=7
for ind1 in range(len(L)-1):
    for ind2 in range(ind1+1,len(L)):
        if L[ind1]+L[ind2]==target:
            print(L[ind1],L[ind2])