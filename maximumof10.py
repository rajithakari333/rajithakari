a=input()
b=list(map(int,a.split(' ')))
b.sort()
print(b[len(b)-1])
