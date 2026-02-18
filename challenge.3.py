regno=int(input("enter two digit registration number"))
a=int(input("enter total no of students"))
marks=[0]*a
valid_count=0
failed_count=0

for i in range(a):
    marks[i] = int(input("enter marks:"))
    if marks[i]<0 or marks[i]>100:
        print(marks[i],"->Invalid")
    else:
      if marks[i]>=regno:
        marks[i]=marks[i]+2
        if marks[i]>100:
          marks[i]=100
      if marks[i]>=90 and marks[i]<=100:
        print(marks[i],"->Excellent")
        valid_count = valid_count + 1
      elif marks[i]>=75 and marks[i]<=89:
        print(marks[i],"->Very Good")
        valid_count = valid_count + 1
      elif marks[i]>=60 and marks[i]<=74:
        print(marks[i],"->Good")
        valid_count = valid_count + 1
      elif marks[i]>=40 and marks[i]<=59:
        print(marks[i],"->Average")
        valid_count = valid_count + 1
      elif marks[i]>=0 and marks[i]<=39:
        print(marks[i],"->Fail")
        valid_count = valid_count + 1
        failed_count = failed_count + 1

print("Total Valid Students:", valid_count)
print("Total Failed Students:",failed_count)
