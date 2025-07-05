m=[[1,2,3],[4,5,6],[7,8,9]]
sum=0
for ind1 in range(len(m)):
    for ind2 in range(len(m)):
        if ind1==ind2:
            sum+=m[ind1][ind2]
print(sum)            