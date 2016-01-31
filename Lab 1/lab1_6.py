str1 = str(raw_input("Enter url:"))
if str1.find("www")!=-1:
    str1 = "http://" + str1
    if str1.find(".com")==-1:
        str1 = str1 + ".com"
        
print str1
raw_input()
    

