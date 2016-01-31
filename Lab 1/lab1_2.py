# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

day = ""
mounth =""
year = ""

def Format(x,length):
    if len(x)<length:
        x = "0" + x
        x = Format(x, length)
    return x

while True:
    try:
        day = raw_input("Enter the day:")
        if int(day)>0 and int(day)<=31:
            day = Format(day, 2)
            break
        else:
            print "Invalid input value"
    except ValueError:
        print "Invalid input value"
    

while True:
    try:
        mounth = raw_input("Enter the mounth:")
        if int(mounth)>0 and int(mounth)<=12:
            mounth = Format(mounth, 2)
            break
        else:
            print "Invalid input value"
    except ValueError:
        print "Invalid input value"
        
while True:
    try:
        year = raw_input("Enter the year:")
        if int(year)>0 and int(year)<=9999:
            year = Format(year, 4)
            break
        else:
            print "Invalid input value"
    except ValueError:
        print "Invalid input value"
        
print day + "/" + mounth + "/" + year
        
raw_input() 