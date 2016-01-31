card_number = 0

while True:
    try:
        card_number = raw_input("Enter the wallet number: ")
        if len(card_number)==16:
            break
    except:
        print "Invalid input format"
        
print card_number[0:4:1]+" **** **** "+card_number[12:16:1]
raw_input()