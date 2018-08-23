a=input()
l=list(map(int,a.split(' ')))
x=l[0]
y=l[1]
x=x^y
y=x^y
x=x^y
print(x,y)
