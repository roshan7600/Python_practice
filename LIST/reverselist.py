L=[1,2,3,4]

# L.reverse()
# print(L)

for ind in range(len(L)//2):
    L[ind],L[-ind-1]=L[-ind-1],L[ind]
print(L)    