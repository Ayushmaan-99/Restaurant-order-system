# Restaurant Order System

A simple command-line ordering system for a restaurant that allows customers to order food, soft drinks, and coffee while keeping track of their bill.

## 📋 Features

- **Multi-Category Menu**: Browse and order from three different categories:
  - 🍔 Food Items (15 options)
  - 🥤 Soft Drinks (15 options)
  - ☕ Coffee (10 options)
- **Easy Ordering**: Simple text-based interface to select items and quantities
- **Automatic Bill Calculation**: Calculates total bill based on item prices and quantities
- **Order Summary**: Displays final order with itemized breakdown
- **Duplicate Item Handling**: Automatically adds quantities if you order the same item twice

## 🏗️ Design Overview

### Architecture
The program follows a simple procedural design with three main data structures:

```
┌─────────────────────────────────────┐
│       Menu Dictionaries             │
├─────────────────────────────────────┤
│  • menu (15 food items)             │
│  • soft_drink (15 beverages)        │
│  • coffee (10 coffee variations)    │
└──────────────────┬──────────────────┘
                   │
                   ▼
┌─────────────────────────────────────┐
│     Ordering Section x3             │
├─────────────────────────────────────┤
│ For each category:                  │
│ 1. Display items with prices        │
│ 2. Loop until user enters 'Done'    │
│ 3. Accept item name & quantity      │
│ 4. Add to order dictionary          │
└──────────────────┬──────────────────┘
                   │
                   ▼
┌─────────────────────────────────────┐
│      Bill Calculation               │
├─────────────────────────────────────┤
│ • Iterate through order items       │
│ • Look up price from correct menu   │
│ • Calculate: price × quantity       │
│ • Sum all items for total bill      │
└─────────────────────────────────────┘
```

### Data Flow

1. **Input**: User selects items and quantities
2. **Storage**: Items stored in `order` dictionary with format: `{item_name: quantity}`
3. **Processing**: Calculate total by matching items to their menus and prices
4. **Output**: Display itemized bill and total amount

### Currency
All prices are in **Indian Rupees (₹)**

## 🍽️ Menu Details

### Food Menu (15 items)
| Item | Price |
|------|-------|
| Burger | ₹200 |
| Pizza | ₹250 |
| Pasta | ₹200 |
| Fries | ₹100 |
| Momo | ₹250 |
| Sandwich | ₹150 |
| Noodles | ₹180 |
| Taco | ₹160 |
| Hotdog | ₹130 |
| Wrap | ₹170 |
| Salad | ₹120 |
| Soup | ₹110 |
| Garlic Bread | ₹90 |
| Paneer Roll | ₹140 |
| Chicken Wings | ₹220 |

### Soft Drinks Menu (15 items)
| Item | Price |
|------|-------|
| Coca Cola | ₹50 |
| Pepsi | ₹50 |
| Sprite | ₹50 |
| Fanta | ₹50 |
| Thumbs Up | ₹55 |
| Mountain Dew | ₹55 |
| 7Up | ₹50 |
| Limca | ₹50 |
| Maaza | ₹45 |
| Appy Fizz | ₹60 |
| Red Bull | ₹120 |
| Monster Energy | ₹150 |
| Bottled Water | ₹20 |
| Iced Tea | ₹70 |
| Lemonade | ₹60 |

### Coffee Menu (10 items)
| Item | Price |
|------|-------|
| Espresso | ₹400 |
| Cappuccino | ₹500 |
| Latte | ₹450 |
| Americano | ₹500 |
| Mocha | ₹660 |
| Macchiato | ₹700 |
| Flat White | ₹690 |
| Cold Brew | ₹200 |
| Café au Lait | ₹900 |
| Affogato | ₹250 |

## 🚀 Installation & Usage

### Requirements
- Python 3.x
- No external dependencies required

## 📝 Sample Output

```
___________________________Welcome to order!_______________________



_______Here's our Items_____

Burger	:	₹200
Pizza	:	₹250
Pasta	:	₹200
Fries	:	₹100
Momo	:	₹250
Sandwich	:	₹150
Noodles	:	₹180
Taco	:	₹160
Hotdog	:	₹130
Wrap	:	₹170
Salad	:	₹120
Soup	:	₹110
Garlic Bread	:	₹90
Paneer Roll	:	₹140
Chicken Wings	:	₹220

Enter the item you want to order (or type 'done'): Burger
How many Burgers would you like? 2

Enter the item you want to order (or type 'done'): Pizza
How many Pizzas would you like? 1

Enter the item you want to order (or type 'done'): Done


_______Here's our Soft Drinks_____


Coca Cola	:	₹50
Pepsi	:	₹50
Sprite	:	₹50
Fanta	:	₹50
Thumbs Up	:	₹55
Mountain Dew	:	₹55
7Up	:	₹50
Limca	:	₹50
Maaza	:	₹45
Appy Fizz	:	₹60
Red Bull	:	₹120
Monster Energy	:	₹150
Bottled Water	:	₹20
Iced Tea	:	₹70
Lemonade	:	₹60

Enter the item you want to order (or type 'done'): Sprite
How many Sprites would you like? 2

Enter the item you want to order (or type 'done'): Done


_______Here's our Coffess_____


Espresso	:	₹400
Cappuccino	:	₹500
Latte	:	₹450
Americano	:	₹500
Mocha	:	₹660
Macchiato	:	₹700
Flat White	:	₹690
Cold Brew	:	₹200
Café au Lait	:	₹900
Affogato	:	₹250

Enter the item you want to order (or type 'done'): Cappuccino
How many Cappuccinos would you like? 1

Enter the item you want to order (or type 'done'): Done


____________________Your Final Order Summary____________________

Burger x 2 = ₹400
Pizza x 1 = ₹250
Sprite x 2 = ₹100
Cappuccino x 1 = ₹500

---------------------------------------------------------------
 Total Bill: ₹1250
Thank you for ordering! Have a great day!
```

## 💡 How It Works

1. **Menu Display**: The program displays items from each category with their prices
2. **Order Placement**: Users enter item names and quantities one by one
3. **Duplicate Handling**: If you order the same item again, the quantities are summed up
4. **Bill Calculation**: The system matches each ordered item to its menu and multiplies by quantity
5. **Summary**: Final order summary shows each item with quantity and total cost

## 🔑 Key Functions

- **Menu Display**: Uses dictionary iteration to show items and prices
- **Input Validation**: Checks if entered item exists in the menu
- **Order Tracking**: Uses dictionary to store and accumulate item quantities
- **Price Lookup**: Searches across all three menus to find correct pricing
- **Bill Calculation**: Iterates through orders to calculate itemized and total costs

## 📌 Notes

- Item names are case-insensitive (uses `.title()` method)
- Enter 'Done' (case-insensitive) to move to the next category
- The system prevents duplicate menu sections in the final bill by checking which menu each item belongs to

---

**Version**: 1.0  
**Language**: Python 3  
**Purpose**: Restaurant ordering system with bill calculation
