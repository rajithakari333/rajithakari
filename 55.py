q=input()
w=list(map(int,q.split(' ')))
r=w[0]*w[1]
if(r%2)==0:
    print("even")
else:
    print("odd")
