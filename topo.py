import numpy as np
import time
filename = input("Enter a input file name:")
#"marschner_lobb_41x41x41_uint8.raw"
#"hydrogenAtom.raw"
dim_x=int(input("Enter the dimension of x:"))
dim_y=int(input("Enter the dimension of y:"))
dim_z=int(input("Enter the dimension of z:"))
A = np.fromfile(filename, dtype='uint8', sep="")
A = A.reshape((dim_x, dim_y, dim_z))
c=int(input("Enter the c value: "))
start = time.time()
v=dim_x*dim_y*dim_z
e=0
a=0
max=0
for i in range(0,dim_x):
    for j in range(0,dim_y):
        for k in range(0,dim_z):
            if(A[i][j][k]>=c):
                if(max<A[i][j][k]):
                    max=A[i][j][k]
                a+=1
                if(i+1 < dim_x):
                    if(A[i+1][j][k]>=c):
                        e+=1
                if(j+1 < dim_y):
                    if(A[i][j+1][k]>=c):
                        e+=1
                if(k+1<dim_z):
                    if(A[i][j][k+1]>=c):
                        e+=1
print("\n")
print('max:',max)
print('no of vertices: ',a)
print('no of edges: ',e)

t=0
arr=[ [0] * int(e) for i in range(int(v))]
for i in range(0,dim_x):
    for j in range(0,dim_y):
        for k in range(0,dim_z):
            if(A[i][j][k]>=c):
                if(i+1 < dim_x):
                    if(A[i+1][j][k]>=c):
                        x=i+j*dim_x+k*dim_x*dim_y
                        y=(i+1)+j*dim_x+k*dim_x*dim_y
                        arr[x][t]=-1
                        arr[y][t]=1
                        t+=1
                if(j+1 < dim_y):
                    if(A[i][j+1][k]>=c):
                        x=i+(j)*dim_x+k*dim_x*dim_y
                        y=(i)+(j+1)*dim_x+k*dim_x*dim_y
                        arr[x][t]=-1
                        arr[y][t]=1
                        t+=1
                if(k+1<dim_z):
                    if(A[i][j][k+1]>=c):
                        x=i+(j)*dim_x+k*dim_x*dim_y
                        y=(i)+(j)*dim_x+(k+1)*dim_x*dim_y
                        arr[x][t]=-1
                        arr[y][t]=1
                        t+=1

rank=np.linalg.matrix_rank(arr)
print("Rank: " + str(rank))
betti_0 = a - rank

print("+---------+")
print('|\N{GREEK SMALL LETTER BETA}\N{SUBSCRIPT ZERO} =',betti_0,'|')
print("+---------+")

end = time.time()
print("\nExecution time:",(end - start))













