m=[[1,2,3],[4,5,6],[7,8,9]]
result=[]
for ind1 in range(len(m)):
    line=[]
    for ind2 in range(len(m)-1,-1,-1):
        line.append(m[ind2][ind1])
    result.append(line)    
print(result)    
