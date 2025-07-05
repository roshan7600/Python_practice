m1=[[1,2],[3,4]]
m2=[[5,6],[7,8]]

result=[]
if (len(m1)==len(m2)) and (len(m1[0])==len(m2)):
    for ind1 in range(len(m1)):
        line=[]
        for ind2 in range(len(m2[0])):
            Add=0
            for ind3 in range(len(m2)):
                Add+=m1[ind1][ind3]*m2[ind3][ind2]
            line.append(Add)    
        result.append(line)    
    print(result)    
else:
    print('not possible')    