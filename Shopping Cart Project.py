# Shopping Cart System - Version 2 
# Includes: Age verification, advanced add/remove, input validation, and clean exit

# Dictionary of common items with their prices
common_items = {
    "Milk": 3.00,
    "Bread": 3.99,
    "Eggs": 7.20,
    "Rice": 5.99,
    "Chicken": 8.99,
    "Apples": 1.99,
    "Bananas": 0.59,
    "Potatoes": 5.59,
    "Onions": 2.29,
    "Tomatoes": 3.99,
    "Pasta": 1.79,
    "Cheese": 4.49,
    "Yogurt": 3.29,
    "Butter": 3.79,
    "Orange Juice": 3.99,
    "Coffee": 7.99,
    "Tea": 3.29,
    "Sugar": 2.49,
    "Flour": 3.19,
    "Cereal": 4.79,
    "Peanut Butter": 5.99,
    "Jelly": 3.49,
    "Cookies": 2.99,
    "Ice Cream": 5.49,
    "Frozen Pizza": 6.99,
    "Ground Beef": 7.49,
    "Salmon": 9.99,
    "Shampoo": 5.99,
    "Soap": 2.49,
    "Toothpaste": 3.79,
    "Toilet Paper": 12.99,
    "Paper Towels": 8.49,
    "Laundry Detergent": 14.99,
    "Dish Soap": 3.49,
    "Sponges": 1.99,
    "Garbage Bags": 6.99,
    "Batteries": 5.49,
    "Light Bulbs": 3.99,
    "Candles": 2.99,
    "Vitamins": 9.99,
    "Pain Reliever": 5.49,
    "Bandages": 3.29,
    "Soda": 5.99,
    "Beer": 12.99,
    "Wine": 15.99,
    "Chips": 3.49,  
    "Crackers": 2.99,
    "Nuts": 5.99,
    "Olive Oil": 14.99,
    "Vinegar": 3.49
}

# Age-restricted items
restricted_items = ["Beer", "Wine"]

# Shopping cart structure: {"Item Name": [price, quantity]}
cart = {}

# Utility function
def confirm_action(message):
    confirm = input(f"{message} (yes/no): ").strip().lower()
    return confirm == "yes"

# Function to display main menu options
def display_menu():
    print("\nSHOPPING CART SYSTEM")
    print("1. Add Common Item")
    print("2. Add Custom Item")
    print("3. Remove Item")
    print("4. View Cart")
    print("5. Checkout")
    print("6. Exit")


# Function to add a common item to the cart
def add_common_items(user_age):
    print("\nCOMMON ITEMS:")
    for i, (item, price) in enumerate(common_items.items(), 1):
        print(f"{i}. {item} - ${price:.2f}")

    try:
        choices = input("Enter item numbers to add (comma-separated): ")
        item_indexes = [int(x.strip()) for x in choices.split(",")]

        for index in item_indexes:
            if 1 <= index <= len(common_items):
                item = list(common_items.keys())[index - 1]
                if item in restricted_items and user_age < 18:
                    print(f"{item} is age-restricted. Skipped.")
                    continue
                quantity = int(input(f"Quantity of {item}: "))
                if item in cart:
                    cart[item][1] += quantity
                else:
                    cart[item] = [common_items[item], quantity]
                print(f"Added {quantity}x {item}")
            else:
                print(f"Invalid item number: {index}")
    except ValueError:
        print("Invalid input! Make sure to enter item numbers separated by commas.")

# Function to add a custom item to the cart
def add_custom_item():
    item = input("\nEnter custom item name: ")
    try:
        price = float(input("Enter item price: "))
        quantity = int(input("Enter item quantity: "))
        if item in cart:
            cart[item][1] += quantity
        else:
            cart[item] = [price, quantity]
        print(f"Added {quantity}x {item} (Custom)")
    except ValueError:
        print("Invalid price or quantity!")

#Function to remove an item from the shopping cart
def remove_item():
    if not cart:
        print("Your cart is empty!")
        return
    
    print("\nCURRENT ITEMS IN CART:")
    for i, item in enumerate(cart.keys(), 1):
        print(f"{i}. {item}")
    
    try:
        choice = int(input("Enter item number to remove: "))
        if 1 <= choice <= len(cart):
            item = list(cart.keys())[choice-1]
            del cart[item]
            print(f"Removed {item}")
        else:
            print("Invalid selection!")
    except ValueError:
        print("Please enter a number!")

# Function to view the current cart with items, prices, and totals
def view_cart():
    if not cart:
        print("Your cart is empty!")
        return
    
    print("\nYour Cart")
    print("-" * 40)
    total = 0

    for item, (price, quantity) in cart.items():
        item_total = price * quantity
        total += item_total
        print(f"{item:<20} {quantity:>3}x ${price:>5.2f} = ${item_total:>6.2f}")

    print ("-" * 40)
    print(f"Total: ${total:.2f}")

# Function to handle checkout process
def checkout():
    view_cart()  # Show final cart
    if cart:
        print("\Thank you for your purchase!")
        cart.clear()  # Clear cart after purchase
    
# Main Loop to run the program
while True:
    display_menu()  # Show menu options
    try:
        choice = int(input("Enter choice (1-6): "))
        if choice == 1:
            add_common_item()
        elif choice == 2:
            add_custom_item()
        elif choice == 3:
            remove_item()
        elif choice == 4:
            view_cart()
        elif choice == 5:
            checkout()
        elif choice == 6:
            print("Goodbye!")
            break  # Exit the loop
        else:
            print("Please enter 1-6")
    except ValueError:
        print("Invalid input! Enter a number 1-6")
# End of the shopping cart system

