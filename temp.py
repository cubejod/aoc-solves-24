with open("day1input.txt") as f:
    data=f.readlines()

arr1=[]
arr2=[]
hm1={}
hm2={}
for i in range(len(data)):
    arr1.append(int(data[i][0:5]))
    if int(data[i][0:5]) in hm1:
        hm1[int(data[i][0:5])]+=1
    else:
        hm1[int(data[i][0:5])]=1
    arr2.append(int(data[i][8:13]))
    if int(data[i][8:13]) in hm2:
        hm2[int(data[i][8:13])]+=1
    else:
        hm2[int(data[i][8:13])]=1
arr1=sorted(arr1)
arr2=sorted(arr2)
op=0
op2=0
for i in range(len(arr1)):
    op+=abs(arr1[i]-arr2[i])
    if arr1[i] in hm2:
        op2+=hm2[arr1[i]]*arr1[i]
print(op)
print(op2)