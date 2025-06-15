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

# List of items that require age verification
restricted_items = ["Beer", "Wine"]

# Shopping cart to hold items as: {"Item Name": [price, quantity]}
cart = {}

# Function to get user's age and validate it
def get_age():
    while True:
        age = eg.enterbox("Enter your age (must be between 5 and 100):")
        if age is None:  # User pressed Cancel
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

# Function to add selected common items to the cart
def add_common_items(user_age):
    # Create display list with item name and price
    item_list = [f"{item} - ${price:.2f}" for item, price in common_items.items()]
    choices = eg.multchoicebox("Select items to add:", "Common Items", item_list)
    if not choices:
        return
    for choice in choices:
        item = choice.split(" - $")[0]
        
        # Block restricted items if user is underage
        if item in restricted_items and user_age < 18:
            eg.msgbox(f"{item} is age-restricted and cannot be added.")
            continue
        
        # Ask for quantity and validate input
        quantity = eg.enterbox(f"How many of {item} would you like to add?")
        if quantity is None:
            continue
        try:
            quantity = int(quantity)
            if quantity <= 0 or quantity > 800:
                raise ValueError
            key = item + " (Common)"
            
            # If item already in cart, increase quantity (if within limit)
            if key in cart:
                if cart[key][1] + quantity > 800:
                    eg.msgbox(f"Cannot add {quantity} more. You already have {cart[key][1]} of {item}. Max per item is 800.")
                    continue
                cart[key][1] += quantity
            else:
                cart[key] = [common_items[item], quantity]
        except:
            eg.msgbox("Invalid quantity. Please enter a whole number between 1 and 800.")

# Function to add a custom item not in the predefined list
def add_custom_item(user_age):
    item = eg.enterbox("Enter custom item name:")
    if item is None or item.strip() == "":
        return
    item = item.strip()

    # Block restricted or duplicate entries
    if item in restricted_items and user_age < 18:
        eg.msgbox(f"'{item}' is age-restricted and cannot be added.")
        return
    if item in common_items:
        eg.msgbox(f"'{item}' is a standard item. You must use the 'Add Common Item' option.")
        return

    # Ask for item price and quantity
    price_input = eg.enterbox(f"Enter the price for {item} (e.g., 3.99):")
    if price_input is None:
        return

    try:
        price = float(price_input)

        quantity_input = eg.enterbox(f"Enter quantity of {item} (1 to 800):")
        if quantity_input is None:
            return
        quantity = int(quantity_input)
        if quantity <= 0 or quantity > 800:
            raise ValueError

        key = item + " (Custom)"
        if key in cart:
            if cart[key][1] + quantity > 800:
                eg.msgbox(f"Cannot add {quantity} more. You already have {cart[key][1]} of {item}. Max per item is 800.")
                return
            cart[key][1] += quantity
        else:
            cart[key] = [price, quantity]
    except:
        eg.msgbox("Invalid input. Please enter a valid price (e.g., 2.99) and quantity (1 to 800).")

# Function to remove item(s) from the cart
def remove_items():
    if not cart:
        eg.msgbox("Your cart is empty.")
        return
    
    # Special handling if only one item is in the cart
    if len(cart) == 1:
        item = list(cart.keys())[0]
        qty_str = eg.enterbox(f"How many of '{item}' would you like to remove? (You have {cart[item][1]})")
        if qty_str is None:
            return
        try:
            qty = int(qty_str)
            if qty <= 0:
                raise ValueError
            if qty > cart[item][1]:
                eg.msgbox(f"You only have {cart[item][1]} of {item}.")
                return
            if qty == cart[item][1]:
                del cart[item]
            else:
                cart[item][1] -= qty
        except:
            eg.msgbox("Invalid input. Please enter a whole number less than or equal to the quantity you have.")
    else:
        # User selects multiple items to remove
        cart_items = [f"{item} ({cart[item][1]}x)" for item in cart]
        choices = eg.multchoicebox("Select items to remove:", "Remove Items", cart_items)
        if not choices:
            return
        for choice in choices:
            item = choice.rsplit(" (", 1)[0]
            qty_str = eg.enterbox(f"How many of '{item}' would you like to remove? (You have {cart[item][1]})")
            if qty_str is None:
                continue
            try:
                qty = int(qty_str)
                if qty <= 0:
                    raise ValueError
                if qty > cart[item][1]:
                    eg.msgbox(f"You only have {cart[item][1]} of {item}.")
                    continue
                if qty == cart[item][1]:
                    del cart[item]
                else:
                    cart[item][1] -= qty
            except:
                eg.msgbox("Invalid input. Please enter a whole number less than or equal to the quantity you have.")

# Function to display all cart contents and the total cost
def view_cart():
    if not cart:
        eg.msgbox("Your cart is empty.")
        return
    msg = ""
    total = 0
    for item, (price, quantity) in cart.items():
        item_total = price * quantity
        total += item_total
        msg += f"{item:<25} {quantity:>3}x ${price:>5.2f} = ${item_total:>6.2f}\n"
    msg += "\n" + "-" * 40 + f"\nTotal: ${total:.2f}"
    eg.textbox("Your Cart", text=msg)

# Function to finalize the purchase and clear the cart
def checkout():
    if not cart:
        eg.msgbox("Your cart is empty.")
        return
        
    view_cart()
    if eg.ynbox("Are you sure you want to checkout"):
        eg.msgbox("Thank you for your purchase!")
        cart.clear()

# Main program loop
def main():
    user_age = get_age()  # Prompt user for their age first
    while True:
        # Main menu buttons
        choice = eg.buttonbox("Choose an option:", "Main Menu", choices=[
            "Add Common Item", "Add Custom Item", "Remove Item",
            "View Cart", "Checkout", "Exit"
        ])
        if choice is None:
            if eg.ynbox("Are you sure you want to exit?"):
                break
            else:
                continue
        elif choice == "Add Common Item":
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

# Run the program
main()