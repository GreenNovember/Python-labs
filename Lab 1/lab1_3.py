# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

amount = 0.0

def Format(x,length):
    if len(x)<length:
        x = "0" + x
        x = Format(x,length)
    return x

while True:
    try:
        amount = float(raw_input("Enter the amount:"))
        if amount>0:
            break
    except ValueError:
        print "Invalid input value"
        
if str(amount).find(".")==-1:
    print amount + "rub 00 kop"
else:
    amount=str(amount).split(".")
    amount[1] = Format(amount[1],2)
    print amount[0] + " rub " + amount[1] + " kop"
	
raw_input()