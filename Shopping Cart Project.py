# Version 3
import easygui as eg

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
cart = {}

# Shopping cart structure: {"Item Name": [price, quantity]}
cart = {}

# Ask user for age and validate
def get_age():
    while True:
        age = eg.enterbox("Enter your age (must be between 5 and 100):")
        if age is None:
            if eg.ynbox("Are you sure you want to exit?"):
                exit()
            continue
        try:
            age = int(age)
            if 5 <= age <= 100:
                return age
            else:
                eg.msgbox("Invalid age. Please enter a number between 5 and 100.")
        except:
            eg.msgbox("Invalid input. Please enter a valid number (e.g., 25).")

# Function to add a common item(s) to the cart
def add_common_items(user_age):
    item_list = [f"{item} - ${price:}" for item, price in common_items.items()]
    choices = eg.multchoicebox("Select items to add:", "Common Items", item_list)
    if not choices:
        return
    for choice in choices:
        item = choice.split(" - $")[0]
        if item in restricted_items and user_age < 18:
            eg.msgbox(f"{item} is age-restricted and cannot be added.")
            continue
        quantity = eg.enterbox(f"How many of {item} would you like to add?")
        if quantity is None:
            continue
        try:
            quantity = int(quantity)
            if quantity <= 0 or quantity > 8000:
                raise ValueError
            key = item + " (Common)"
            if key in cart:
                cart[key][1] += quantity
            else:
                cart[key] = [common_items[item], quantity]
        except:
            eg.msgbox("Invalid quantity. Please enter a whole number between 1 and 800.")

# Function to add a custom item to the cart
def add_custom_item():
    item = input("\nEnter custom item name: ")
    try:
        price = float(input("Enter item price: "))
        quantity = int(input("Enter item quantity: "))
        if quantity <= 0:
            print("Quantity must be greater than 0. Please try again.")
            return
        if quantity > 800:
            print("You cannot add more than 800 units of an item. Please try again.")
            return
        if item in cart:
            cart[item][1] += quantity
        else:
            cart[item] = [price, quantity]
        print(f"Added {quantity}x {item} (Custom)")
    except ValueError:
        print("Invalid price or quantity!")

# Function to remove an item from the shopping cart
def remove_items():
    if not cart:
        print("Your cart is empty!")
        return

    print("\nCURRENT ITEMS IN CART:")
    for i, item in enumerate(cart.keys(), 1):
        print(f"{i}. {item} ({cart[item][1]}x)")

    try:
        choices = input("Enter item numbers to remove (comma-separated): ")
        item_indexes = [int(x.strip()) for x in choices.split(",")]

        for index in item_indexes:
            if 1 <= index <= len(cart):
                item = list(cart.keys())[index - 1]
                qty = int(input(f"How many of {item} would you like to remove? "))
                if qty >= cart[item][1]:
                    del cart[item]
                    print(f"Removed all of {item}")
                else:
                    cart[item][1] -= qty
                    print(f"Removed {qty}x {item}")
            else:
                print(f"Invalid item number: {index}")
    except ValueError:
        print("Invalid input! Make sure to enter valid numbers.")

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

    print("-" * 40)
    print(f"Total: ${total:.2f}")

# Function to handle checkout process
def checkout():
    if not cart:
        print("Your cart is empty!")
        return
    view_cart()
    if confirm_action("Are you sure you want to checkout?"):
        print("Thank you for your purchase!")
        cart.clear()
        exit()

# Main loop 
def main():
    user_age = get_ages()
    while True:
        choice = eh.buttonbox("Choose an option:", "Main Menu", choices=[
            "Add Common Item", "Add Custom Item", "Remove Item",
            "View Cart", "Checkout", "Exit"
        ])
        if choice is None:
            if eg.ynbox("Are you sure you want to exit?"):
                break
            else:
                continue
        elif choice == "Add Commn Item":
            add_common_items(user_age)
        elif choice == "Add Custom Item":
            add_custom_item(user_age)
        elif choice == "Remove Item":
            remove_items()
        elif choice == "View Cart":
            view_cart()
        elif choice == "Checkout":
            checkout()
        elif choice == "Exit":
            if eg.ynbox("Are you sure you want to exit?"):
                break
