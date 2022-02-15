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
