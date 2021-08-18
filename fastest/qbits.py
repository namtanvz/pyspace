n = int(input())
s = input()
if s == "byte":n*=8
elif s == "KB":n*=1024*8
elif s == "MB":n*=1024*1024*8
elif s == "GB":n*=1024*1024*1024*8
elif s == "TB":n*=1024*1024*1024*1024*8
r = 0
while 2**r<n:r+=1
print(r)
/ ------------------------------------ /
n = int(input())
s = input()

c = ["KB","MB","GB","TB"]
if s == "byte":
    f = n*8
else:
    p = c.index(s)
    f = n*8*1024**(p+1) 

i = 1
g = 1
while g < f:
    g*=2
    i+=1
print(i-1)
