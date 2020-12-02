import json
l=['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
n=int(input("Input: "))
n1=list(map(int,str(n)))
n1=[x-2 for x in n1]
i=list(l[n1[0]])
j=list(l[n1[1]])
l1=["{}{}".format(x,y) for y in j for x in i]
print(f"Output: {json.dumps(l1)}")
