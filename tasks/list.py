L1=[[1,2,3],[4,5,6],[7,8,9]]
L2=[[9,8,7],[6,5,4],[3,2,1]]
for i in range(len(L1)):
    for j in range(len(L1)):
        print(L1[i][j]+L2[i][j],end=' ')
    print(' ') 