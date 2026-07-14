h,m=map(int,input().split())
time=h*60+m
time-=45
if (time<0):
    time+=24*60

a=int(time/60)
b=time%60
print(a," ",b)