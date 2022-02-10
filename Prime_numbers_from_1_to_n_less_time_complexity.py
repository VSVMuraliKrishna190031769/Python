n=int(input())
a=[1];a=a*(n+1)
i=2
while i<=n+1:
    for j in range(2,n//i + 1):
        a[i*j]=0
    i+=1
for i in range(2,n+1):
    if a[i]==1:
        print(i,end=" ")
