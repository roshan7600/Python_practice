m=[[1,2,3],[4,5,6],[7,8,9]]
result=[]
for ind1 in range(len(m)-1,-1,-1):
    line=[]
    for ind2 in range(len(m)-1,-1,-1):
        line.append(m[ind1][ind2])
    result.append(line)    
print(result)    
