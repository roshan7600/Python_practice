L=[1,4,6,25,9,3,10,23]
n=len(L)

for ind1 in range(n):
    for ind2 in range(n-ind1-1):
        if L[ind2] > L[ind2+1]:
            L[ind2],L[ind2+1]=L[ind2+1],L[ind2]
print(L[-2])            