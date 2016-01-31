mas2 = [1,8,3,4,5,6,7,8,9,10,11]
flag = True
n=1
while n < len(mas2):
    for i in range(len(mas2)-n):
        if int(mas2[i])> int(mas2[i+1]):
            flag = False
    n+=1
if (flag==False):
    print "FALSE"
else:
    print "TRUE"
raw_input()