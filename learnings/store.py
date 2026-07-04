sum = 0
items = []
while(True):
    ui = input("Eneter the item name or press 'q' to get reciept: \n")
    if ui!='q':
        price = float(input(f"Price of {ui} is ₹"))
        sum += price
        items.append((ui,price))
    else:
        print("RECIEPT")
        print("-"*30)
        for i,price in items:
            print(f"{i:20} ₹{price:.2f}")
        print("-"*30)
        print(f"{'Total':20} ₹{sum:.2f}")
        break


    

