'''
You are given a binary string S and an integer K. In one operation, you can pick any bit and flip it, i.e turn 0 to 1 or 1 to 0. 
Can you make the string S a palindrome using exactly K operations?

Print YES if this is possible, and NO if it is not.

Sample Input :
2
3 0
110
6 1
101100
Sample Output :
NO
YES
'''
t=int(input())
for i in range(t):
    n,k=map(int,input().split()) 
    s=list(input()) 
    if k==0:
        if s==s[::-1]:
            print('YES')
        else:
            print('NO') 
        continue
    i=0 
    j=len(s)-1
    while(i<j):
        if s[i]!=s[j]:
            s[i]=s[j]
            k-=1
        if k==0:
            if s==s[::-1]:
                print('YES')
            else:
                print('NO')
            break 
        i+=1
        j-=1
    if k!=0:
        if s==s[::-1]:
            if len(s)%2==0 and k%2!=0:
                print('NO')
            else:
                print('YES')
        else:
            print('NO')