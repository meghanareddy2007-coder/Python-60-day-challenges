name=input("enter your  full name :")
email=input("enter your email :")
mobile_number=input("enter your mobile number :")
age=int(input("enter your age :"))
if(name != "" and name[0]!=" " and name[len(name)-1] !=" " and name.count(" ") >=1 and
   email.count("@") >=1 and email.count(".")>=1 and email[0]!='@'  and
   mobile_number[0]!='0'and mobile_number.isdigit()  and len(mobile_number)==10 and
   age>= 18 and age <=60 ):
    print(" User Profile is VALID")
else:
    print("User Profile is NOT VALID")

