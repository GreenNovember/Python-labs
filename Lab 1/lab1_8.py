mas = str(raw_input("Enter the word:")).split(" ")
mas2 = []
for k in mas:
    if (len(k.strip())>0):
        mas2.append(k.strip())
print [str(k) for k in mas2]

n=1
while n < len(mas2):
    for i in range(len(mas2)-n):
        if len(mas2[i])< len(mas2[i+1]):
            mas2[i], mas2[i+1] = mas2[i+1], mas2[i]
    n+=1
    
print [str(k) for k in mas2]
raw_input()