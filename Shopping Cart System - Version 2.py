# Shopping Cart System - Version 2

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

# List of items that are age-restricted (18+ only)
restricted_items = ["Beer", "Wine"]

# The shopping cart is a dictionary: {"Item Name": [price, quantity]}
cart = {}

# Utility function to confirm user actions with a yes/no prompt
def confirm_action(message):
    confirm = input(f"{message} (yes/no): ").strip().lower()
    return confirm == "yes"

# Displays the main menu of options
def display_menu():
    print("\nSHOPPING CART SYSTEM")
    print("1. Add Common Item")
    print("2. Add Custom Item")
    print("3. Remove Item")
    print("4. View Cart")
    print("5. Checkout")
    print("6. Exit")

# Allows the user to add pre-defined items to their cart
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
                if quantity <= 0:
                    print("Quantity must be greater than 0. Please try again.")
                    continue
                if quantity > 800:
                    print("You cannot add more than 800 units of an item. Please try again.")
                    continue
                if item in cart:
                    cart[item][1] += quantity
                else:
                    cart[item] = [common_items[item], quantity]
                print(f"Added {quantity}x {item}")
            else:
                print(f"Invalid item number: {index}")
    except ValueError:
        print("Invalid input! Make sure to enter item numbers separated by commas.")

# Allows the user to add a custom item by typing its name, price, and quantity
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

# Lets user remove items or reduce quantity of items in their cart
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

# Displays a summary of all items in the cart with totals
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

# Processes the checkout, confirms, shows total, and clears the cart
def checkout():
    if not cart:
        print("Your cart is empty!")
        return
    view_cart()
    if confirm_action("Are you sure you want to checkout?"):
        print("Thank you for your purchase!")
        cart.clear()
        exit()

# Confirms with the user before exiting the program
def exit_program():
    if confirm_action("Are you sure you want to exit?"):
        print("Goodbye!")
        exit()

# Gets the user's age and ensures it's within allowed limits (5–100)
def main():
    print("Welcome to the Shopping Cart System!")
    while True:
        try:
            user_age = int(input("Please enter your age: "))
            if user_age < 5 or user_age > 100:
                print("Age must be between 5 and 100.")
                continue
            return user_age
        except ValueError:
            print("Please enter a valid number for age.")

# Start the program by getting the user's age
user_age = main()

# Loop through the menu until the user chooses to exit
while True:
    display_menu()
    try:
        choice = int(input("Enter choice (1-6): "))
        if choice == 1:
            add_common_items(user_age)
        elif choice == 2:
            add_custom_item()
        elif choice == 3:
            remove_items()
        elif choice == 4:
            view_cart()
        elif choice == 5:
            checkout()
        elif choice == 6:
            exit_program()
            break
        else:
            print("Invalid input! Enter a number 1-6")
    except ValueError:
        print("Invalid input! Enter a number 1-6")
