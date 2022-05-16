n=int(input())
list=[]
for i in range(n):
    list.append(input().split())
p=[3,2,35,4]   
a=0
for i in range(len(list)):
    if int(list[i][0]) >= p[0] and int(list[i][1]) >= p[1] and int(list[i][2]) < p[2] and int(list[i][3]) >= p[3]:
        print(list[i][4])
        a+=1
if a == 0:
    print('NO DISPONIBLE')