import numpy as np

c1 = [1,1,1,1]
c2 = [1,-1,1,-1]
c3 = [1,-1,-1,1]
c4 = [1,1,-1,-1]

print("Enter the data bits:")
d1 = int(input("Enter d1:"))
d2 = int(input("Enter d2:"))
d3 = int(input("Enter d3:"))
d4 = int(input("Enter d4:"))

r1 = np.multiply(c1,d1)
r2 = np.multiply(c2,d2)
r3 = np.multiply(c3,d3)
r4 = np.multiply(c4,d4)

resultantChannel = r1+r2+r3+r4
print("resultant channel:",resultantChannel)

rc=[]
channel = int(input("Enter the station to listen for c1=1, c2=2, c3=3, c4=4:"))
if channel==1:
    rc=c1
elif channel==2:
    rc=c2
elif channel==3:
    rc=c3
else:
    rc=c4
innerProduct = np.multiply(rc,resultantChannel)
print("inner product:", innerProduct)

data = sum(innerProduct)/len(innerProduct)
print("data bit that was sent:",data)