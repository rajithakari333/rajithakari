p=input()
w=list(map(int,p.split(' ')))
q=w[0]*w[1]
if(q%2)==0:
    print("even")
else:
    print("odd")
