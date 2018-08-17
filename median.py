from statistics import median
n = int(input())
arr = input()
l = list(map(int,arr.split(' ')))
n=len(l)
print(median(l))
