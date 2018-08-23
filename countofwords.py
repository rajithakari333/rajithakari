def count():
    fullname=input(" ").split()
    total=0
    for x in fullname:
        total +=len(x)
    print(total)
count()
