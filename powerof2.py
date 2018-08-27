def isp(n):
   if(n==0):
      return false
   else:
      for i in range(n):
          i=2**i
          if(i==n):
               print("yes")
               break
      else:
          print("no")
s=int(input())
isp(s)
