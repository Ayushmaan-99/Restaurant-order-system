menu =  {
    "Burger": 200,
    "Pizza": 250,
    "Pasta": 200,
    "Fries": 100,
    "Momo": 250,
    "Sandwich": 150,
    "Noodles": 180,
    "Taco": 160,
    "Hotdog": 130,
    "Wrap" : 170,
    "Salad": 120,
    "Soup" : 110,
    "Garlic Bread": 90,
    "Paneer Roll": 140,
    "Chicken Wings": 220
}

soft_drink = {
    "Coca Cola": 50,
    "Pepsi": 50,
    "Sprite": 50,
    "Fanta": 50,
    "Thumbs Up": 55,
    "Mountain Dew": 55,
    "7Up": 50,
    "Limca": 50,
    "Maaza": 45,
    "Appy Fizz": 60,
    "Red Bull": 120,
    "Monster Energy": 150,
    "Bottled Water": 20,
    "Iced Tea": 70,
    "Lemonade": 60
}

coffee = {
   "Espresso" : 400,
   "Cappuccino" : 500,
   "Latte" : 450,
   "Americano" : 500,
   "Mocha" : 660,
   "Macchiato" : 700,
   "Flat White" : 690,
   "Cold Brew" : 200,
   "Café au Lait" : 900,
   "Affogato" : 250
}
order = {} # This is a empty dict

print("\n\n\n_________________________Welcome to order!_______________________\n\n\n")
print("_______Here's our Items_____\n")
for item, price in menu.items():    # here's printing the menu and price 'dict -> key and value'
    print(f"{item}\t:\t₹{price}")   # printing the item first then price
while True:       # while loop start
    choice = input("\nEnter the item you want to order (or type 'done'): ").title()
    
    if choice == 'Done':   # if 'done' typed by user then loop will break
        break
    elif choice in menu:   # finding item in 'menu'
        try:
            qty = int(input(f"How many {choice}s would you like? "))
            if qty <= 0:
                print("Please enter a positive number.")
                continue
            if choice in order:  # adding choice "items" in order
                order[choice] += qty  # adding item quantity
            else:
                order[choice] = qty
        except ValueError:
            print("Invalid input! Please enter a valid number.")
    else:
        print("Sorry, that item is not on the menu.")



print("\n\n_______Here's our Soft Drinks_____\n\n")
for item, price in soft_drink.items():  # here's printing the soft_drink and price 'dict -> key and value'
    print(f"{item}\t:\t₹{price}")    # printing the item first then price
while True:  # while loop start
    choice = input("\nEnter the item you want to order (or type 'done'): ").title()  # Use to pass the upper and lower case
    
    if choice == 'Done':  # if 'done' typed by user then loop will break
        break
    elif choice in soft_drink:   # finding item in 'soft_drink'
        try:
            qty = int(input(f"How many {choice}s would you like? "))
            if qty <= 0:
                print("Please enter a positive number.")
                continue
            if choice in order:  # adding choice "items" in order
                order[choice] += qty   # adding item quantity
            else:
                order[choice] = qty
        except ValueError:
            print("Invalid input! Please enter a valid number.")
    else:
        print("Sorry, that item is not on the menu.")



print("\n\n_______Here's our Coffee_____\n\n")
for item, price in coffee.items():  # here's printing the coffee and price 'dict -> key and value'
    print(f"{item}\t:\t₹{price}")   # printing the item first then price
while True:   # while loop start
    choice = input("\nEnter the item you want to order (or type 'done'): ").title()
    
    if choice == 'Done':  # if 'done' typed by user then loop will break
        break
    elif choice in coffee:    # finding item in 'coffee'
        try:
            qty = int(input(f"How many {choice}s would you like? "))
            if qty <= 0:
                print("Please enter a positive number.")
                continue
            if choice in order:  # adding choice "items" in order
                order[choice] += qty   # adding item quantity
            else:
                order[choice] = qty
        except ValueError:
            print("Invalid input! Please enter a valid number.")
    else:
        print("Sorry, that item is not on the menu.")




# Calculate the bill 

total_bill = 0    # assigning bill to 0 for multiplication

print("\n\n____________________Your Final Order Summary____________________\n")
for item, qty in order.items():  # itrating item and quentity from order list
    if item in menu:
        price = menu[item]
    elif item in soft_drink:
        price = soft_drink[item]
    elif item in coffee:
        price = coffee[item]
    else:
        continue
    item_total = price * qty  
    total_bill += item_total
    print(f"{item} x {qty} = ₹{item_total}")

print("\n---------------------------------------------------------------")
print(f" Total Bill: ₹{total_bill}") # 
print("Thank you for ordering! Have a great day!")