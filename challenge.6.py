n=int(input("Enter number of transactions :"))
transactions=[0]*n
for i in range(n):
    transactions[i]=int(input("Enter transaction amount:"))
categories={
    "normal":[0]*n,
    "large":[0]*n,
    "high_risk":[0]*n,
    "invalid":[0]*n
}
no=0
la=0
high=0
inv=0
for i in range(n):
    t=transactions[i]
    if t<=0:
        categories["invalid"][inv]=t
        inv=inv+1
    elif t>=1 and t<=500:
        categories["normal"][no]=t
        no=no+1
    elif t>500 and t<=2000:
        categories["large"][la]=t
        la=la+1
    elif t>2000:
        categories["high_risk"][high]=t
        high=high+1
print("categorised transactions ")
print("normal:",categories["normal"][:no])
print("large:",categories["large"][:la])
print("high_risk:",categories["high_risk"][:high])
print("invalid:",categories["invalid"][:inv])
valid_transactions=[t for t in transactions if t>0]
total_value=sum(valid_transactions)
number_transactions=len(transactions)
summary=(total_value,number_transactions)
print("transaction summary:",summary)
print("total transaction value:",total_value)
print("number of transactions:",number_transactions)
if number_transactions>5:
    frequent_transactions=True
else:
    frequent_transactions=False
if total_value>5000:
    large_spending=True
else:
    large_spending=False
if high>=3:
    suspicious_pattern=True
else:
    suspicious_pattern=False
risk_score=0
if frequent_transactions:
    risk_score=risk_score+1
if large_spending:
    risk_score=risk_score+1
if suspicious_pattern:
    risk_score=risk_score+1
if risk_score==0:
    risk="Low Risk"
elif risk_score==1:
    risk="Moderate Risk"
else:
    risk="High Risk"
print("Risk:",risk)
if risk=="Low Risk":
    print("Status:Transactions look safe ")
elif risk=="Moderate Risk":
    print("Status:Be cautious, unusual activity detected ")
elif risk=="High Risk":
    print("Status:Alert! suspicious transaction detected ")


