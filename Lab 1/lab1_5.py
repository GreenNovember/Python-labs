
i = 0
j = 0
mass = []

while i<10:
    j = 0
    while j<10:
        if int(i+j)%7==0 and  int(str(i)+str(j))>10:
            mass.append(str(i)+str(j))
        j+=1
    i+=1
print [str(k) for k in mass]
    
raw_input()
