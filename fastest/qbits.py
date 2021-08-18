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
