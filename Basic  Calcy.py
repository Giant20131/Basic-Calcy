print ("Welcome to the Basic Calcy ")

Num1= input("ENTER FIRST NO. FOR THE CALCULATION:")
Num2 = input("ENTER SECOND NO. FOR THE CALCULATION:")
Oprator = input("ENTER THE OPERATION FOR THE CALCULATION (+,-,*,/): ")

Num1 = int(Num1)
Num2 = int(Num2)

if Oprator =="+" : 
    print ("Solution :", Num1 + Num2)
    
if Oprator =="-" :
    print ("Solution :", Num1 - Num2)
    
if Oprator =="*" :
    print ("Solution :", Num1 * Num2)
    
if Oprator =="/" :
    print ("Solution :", Num1 / Num2)   
    