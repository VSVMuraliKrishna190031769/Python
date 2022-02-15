Consider two arrays a,b consisting n number of strings. Your task is to compare two strings a[i], b[i], and determine whether they are comparable.
Two strings are comparable if the subtraction of the number of similar characters doesn't exceed 3. All the strings contain characters of lower case only.
Sample Input:
a=[aaab,abba]
b=[aabba,ddddab]
output:
['YES', 'NO']
Explanation: 
In a[0] and b[0] we get,
3a -3a = 0a
0<3
1b-2b=1b
1<3
All are satisfied so yes 
In a[1] and b[1]
2a-1a=1a
1<3
0d-4d=4d
4>3
Not satisfies
'NO'


def output(l,m):
    k=len(l)
    answer=[]
    for i in range(k):
        flagger=0
        d={}
        e={} 
        for j in m[i]:
            if j not in d:
                d[j]=1
            else:
                d[j]+=1
        for j in l[i]:
            if j not in e:
                e[j]=1
            else:
                e[j]+=1
        for j in e:
            if j not in d:
                if e[j]>3:
                    flagger=1
                    answer.append('NO')
                    break
        if flagger==0:
            for j in d:
                if j in e:
                    if abs(e[j]-d[j])>3:
                        answer.append('NO')
                        flagger=1
                        break
                else:
                    if d[j]>3:
                        answer.append('NO')
                        flagger=1
                        break 
        if flagger==0:
            answer.append('YES')
    return answer

a=['aaab','abba']
b=['aabba','ddddab']
print(output(a,b))