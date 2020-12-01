n=int(input("Room:"))
n1=list(map(int,str(n*n)))
l=len(n1)
l1,r1=0,0
for i in range(l):
    if(i<l//2):
        l1*=10
        l1+=n1[i]
    else:
        r1*=10
        r1+=n1[i]
sum=l1+r1
if sum == n and n%3 ==0:
    print("Status: Safe")
else:
    print("Status: Not safe")