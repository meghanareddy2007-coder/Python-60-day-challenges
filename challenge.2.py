ID = input("Enter Student ID : ")
EmailID= input("Enter Student Email ID: ")
password = input("Enter Student Password: ")
Referral_code=input("Enter Referral Code: ")
if( len(ID) == 7 and ID[0]=='C' and ID[1]=='S' and ID[2]=='E'  and ID[3]=='-' and
    ID[4].isdigit() and ID[5].isdigit() and ID[6].isdigit() and EmailID.count('@') >=1
    and EmailID[0]!='@' and EmailID[len(EmailID)-1]!='@' and  len(EmailID)>=4 and
    EmailID[len(EmailID)-4]=='.' and EmailID[len(EmailID)-3]=='e' and
    EmailID[len(EmailID)-2]=='d' and EmailID[len(EmailID)-1]=='u' and len(password) >=8 and
    password[0].isupper() and  (password.count('0') > 0 or password.count('1') > 0 or
    password.count('2') > 0 or password.count('3') > 0 or password.count('4') > 0
    or password.count('5') > 0 or password.count('6') > 0  or password.count('7') > 0 or
    password.count('8') > 0 or password.count('9') > 0) and Referral_code[0] == 'R'
    and Referral_code[1] == 'E' and  Referral_code[2] == 'F' and Referral_code[3].isdigit() and
    Referral_code[4].isdigit() and Referral_code[len(Referral_code)-1]=='@'):
    print("APPROVED")
else:
    print("REJECTED")