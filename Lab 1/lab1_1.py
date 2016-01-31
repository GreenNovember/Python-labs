# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

if __name__ == "__main__":
    print "Hello World"

x = 0
while True:
    x = raw_input("Input digit:")
    if int(x)>0 and int(x)<100:
        break
    else:
        print "Invalid digit"
        
if int(x)%10==0 or (int(x)>10 and int(x)<20):
    print x + "let"

if ((int(x)-1)%10==0):
        print x + "god"
        
if (((int(x)-2)%10==0)
    or ((int(x)-3)%10==0) 
    or ((int(x)-4)%10==0)) and (int(x)>20):
        print x + "goda"
      
if (((int(x)-5)%10==0) 
    or ((int(x)-6)%10==0) 
    or ((int(x)-7)%10==0) 
    or ((int(x)-8)%10==0)  
    or ((int(x)-9)%10==0)):
        print x + "let"     