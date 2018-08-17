def largest(arr,n):
    max=arr[0]
    for i in range(1,n):
        if arr[i]>max:
            max=arr[i]
    return max
n = int(input())
arr = input()
l = list(map(int,arr.split(' ')))
n=len(l)
ans=largest(l,n)
print(ans)
