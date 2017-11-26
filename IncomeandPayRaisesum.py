def InputValue(Value,Line1):
    while True:
        Value=input(Line1)
        try:
            Value=(int(Value))
            break
        except ValueError:
            try:
                Value=(float(Value))
                break
            except ValueError:
                print("Enter a number please.")
    return Value
                
def Raise(Current,Add):
    if int(Current+Add)==float(Current+Add):
        New=int(Current+Add)
    else:
        New=float(Current+Add)
    return New

Income=0
PayRaise=0

Income=InputValue(Income,"How much do you earn an hour? ")
print("Your current income is","$"+str(Income)+".")

PayRaise=InputValue(PayRaise,"How much is the pay raise? ")        
print("Raise is $"+str(PayRaise)+".")

Income=Raise(Income,PayRaise)
print("Your new income is","$"+str(Income)+", .")

