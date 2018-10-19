import time
scale=20
print("starting")
t=time.clock()
for i in range(scale+1):
    a ="*"*i
    b ="."*(scale-1)
    c =(i/scale)*100
    t -= time.clock()
    print("\r{:^3.0f}%[{}-.{}]{:.2f}s".format(c,a,b,-t),\
          end="")
    time.sleep(0.05)
print("\n"+"Done!".center(scale//2,"-"))
