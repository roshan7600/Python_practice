L1=[1,3,4,7,8,10]
L2=[4,7,13,10]
L0=[]
for ele in L1:
    if ele in L2:
        L0.append(ele)
print(L0)        