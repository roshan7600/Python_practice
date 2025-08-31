m1=[[1,2],[0,1]]
m2=[[0,1],[2,1]]

if (len(m1)!=0 or len(m2)!=0) and (len(m1)==len(m2)) and len(m1[0])==len(m2[0]):
    for ind1 in range(len(m1)):
        for ind2 in range(len(m1[0])):
            m1[ind1][ind2]+=m2[ind1][ind2]
    else:
        print(m1)        
else:
    print('not possible')        