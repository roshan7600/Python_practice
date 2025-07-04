L=[1,4,6,9]
var=max(L)
L0=[]
for ele in range(1,var):
    if ele not in L:
        L0.append(ele)
print(L0)        
