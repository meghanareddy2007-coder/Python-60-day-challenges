name=input("enter your full name:")
L=0
for i in name:
    if i!=" ":
     L=L+1
PLI=L%3
print("L value is ",L)
print("PLI value is ",PLI)
n=int(input("enter number of request values "))
requests=[0]*n
for i in range(n):
    requests[i]=int(input("enter the request value  "))
low_demand=[0]*n
moderate_demand=[0]*n
high_demand=[0]*n
invalid_requests=[0]*n
l=0
m=0
h=0
inv=0
valid=0
for i in range(n):
    request=requests[i]
    if request<0:
        invalid_requests[inv]=request
        inv=inv+1
    elif request==0:
        valid=valid+1
    else:
        valid=valid+1
        if request >=1 and request <=20:
            low_demand[l]=request
            l=l+1
        elif request >=21 and request <=50:
            moderate_demand[m]=request
            m=m+1
        elif request > 50:
            high_demand[h]=request
            h=h+1
print("BEFORE PERSONALISATION :")
print("Low_Demand",low_demand[:l])
print("Moderate_Demand",moderate_demand[:m])
print("High_Demand",high_demand[:h])
print("Invalid Requests",invalid_requests[:inv])
removed_count=0
if PLI==0:
    print("Applied Rule A: Remove All Low Demand Requests")
    removed_count=l
    l=0
elif PLI==1:
    print("Applied Rule B: Remove All High Demand Requests")
    removed_count=h
    h=0
elif PLI==2:
    print("Applied Rule C: Keep only Moderate Demand Requests")
    removed_count=l+h
    l=0
    h=0
print("AFTER PERSONALISATION :")
print("Low_Demand",low_demand[:l])
print("Moderate_Demand",moderate_demand[:m])
print("High_Demand",high_demand[:h])
print("Invalid Requests",invalid_requests[:inv])
print("valid requests:",valid)
print("removed requests:",removed_count)



