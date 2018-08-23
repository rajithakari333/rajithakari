result=[]
n=int(input(""))
a,b=0,1
while b<=n:
    result.append(b)
    a,b=b,a+b
m=(str(result)[1:-1])
print(m.replace(',',' '))
