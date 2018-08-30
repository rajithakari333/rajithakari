myinteger = int(input())
number_string = str(myinteger)
a=[]
for ch in number_string:
    a.append(ch)
m=(str(a)[1:-1])
ch=(m.replace("'",''))
print(ch.replace(',',' '))
