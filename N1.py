a=[[5,-2,5],[2,2,5],[1,2,2]]
b=[2,0,-1]
x=[0,0,0]
t1=[0,1,2]
t2=[2,1,0]
t3=[1,2]
t4=[2,1]
i=0
j=0
for i in t1:
    b[i] = b[i] / a[i][0]
    for j in t2:
        a[i][j]=(a[i][j])/(a[i][0])
for i in t3:
    b[i] = b[i]-b[0]
    for j in t1:
        a[i][j]=a[i][j]-a[0][j]
for i in t3:
    b[i] = b[i] / a[i][1]
    for j in t2:
        a[i][j] = (a[i][j]) / (a[i][1])
for j in t1:
    i=2
    a[i][j]=a[i][j]-a[1][j]
b[i] = b[i]-b[1]
z=b[2]/a[2][2]
y=b[1]-(z*a[1][2])
x=b[0]+(y*0.4)-z
print(x,y,z)