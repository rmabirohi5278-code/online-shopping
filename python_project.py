from getpass import getpass

VALID_ID = "shopping"
VALID_PASSWORD = "miniproject"
VALID_EMAIL = "onlineshopping01@gmail.com"

products = {
    'Sofa': ('HomeTown', 18999),
    'Dining Table': ('Godrej Interio', 22499),
    'Chair 1': ('Nilkamal', 1299),
    'Chair 2': ('IKEA', 1999),
    'Chair 3': ('Durian', 2499),
    'Bed': ('Urban Ladder', 15999),
    'Wardrobe': ('IKEA', 12499),
    'Study Table': ('Durian', 6999),
    'Bookshelf': ('Godrej Interio', 8499),
    'Recliner': ('HomeTown', 11999),
    'T-shirt Puma': ('Puma', 899),
    'T-shirt Adidas': ('Adidas', 999),
    'T-shirt H&M': ('H&M', 799),
    'Jeans': ('Levi’s', 2499),
    'Jacket': ('Adidas', 3299),
    'Kurti': ('Biba', 1199),
    'Hoodie': ('H&M', 1499),
    'Saree': ('Sabyasachi', 14999),
    'Shorts': ('Nike', 1199),
    'Formal Shirt': ('Arrow', 1999),
    'Watch 1': ('Titan', 3499),
    'Watch 2': ('Fastrack', 1599),
    'Watch 3': ('Casio', 4299),
    'Belt': ('Woodland', 899),
    'Handbag': ('Lavie', 2199),
    'Sunglasses': ('Ray-Ban', 7499),
    'Wallet': ('Wildcraft', 799),
    'Earrings': ('Zaveri Pearls', 499),
    'Cap': ('Puma', 699),
    'Bracelet': ('Voylla', 899),
    'Samsung A55': ('Samsung', 27999),
    'Redmi Note 13 Pro': ('Redmi', 20999),
    'Vivo V29': ('Vivo', 29499),
    'Laptop HP Pavilion': ('HP', 54999),
    'Headphones': ('Sony', 2999),
    'Smartwatch': ('Fire-Boltt', 1999),
    'Bluetooth Speaker': ('JBL', 3499),
    'Tablet': ('Lenovo', 12999),
    'Power Bank': ('Mi', 1499),
    'Gaming Mouse': ('Logitech', 2499)
}

def build_categories(products):
    return {
        "Furniture": {k: v for k, v in products.items() if k in {
            'Sofa','Dining Table','Chair 1','Chair 2','Chair 3','Bed','Wardrobe','Study Table','Bookshelf','Recliner'}},
        "Clothes": {k: v for k, v in products.items() if any(prefix in k for prefix in ('T-shirt','Jeans','Jacket','Kurti','Hoodie','Saree','Shorts','Formal'))},
        "Accessories": {k: v for k, v in products.items() if k in {'Watch 1','Watch 2','Watch 3','Belt','Handbag','Sunglasses','Wallet','Earrings','Cap','Bracelet'}},
        "Electronics": {k: v for k, v in products.items() if k in {'Samsung A55','Redmi Note 13 Pro','Vivo V29','Laptop HP Pavilion','Headphones','Smartwatch','Bluetooth Speaker','Tablet','Power Bank','Gaming Mouse'}}
    }

CATEGORIES = build_categories(products)

cart = []   
order = {}

def print_table(title, data):
    print("\n" + title.upper())
    print(f"{'Item':30} {'Brand':20} {'Price'}")
    print("-" * 65)
    for item, (brand, price) in data.items():
        print(f"{item:30} {brand:20} ₹{price}")
    print("-" * 65)

def find_product_by_name(product_name):
    for name, (brand, price) in products.items():
        if name.lower() == product_name.lower():
            return name, brand, price
    return None
def login():
    print("\n=== LOGIN ===")
    while True:

        login_id = input("Login ID: ").strip()
        if login_id != VALID_ID:
            while True:
                retry = input("Retry ID: ").strip()
                if retry==VALID_ID:
                    break
                elif retry!=VALID_ID:
                    pass
            break
        elif login_id==VALID_ID:
            break   
    pin = getpass("Password: ").strip()

    if pin == VALID_PASSWORD:
        print("Login successful.")
        return True

    attempts_left = 4
    for i in range(attempts_left):
        retry_pass = getpass(f"Retry Password (attempt {i+1}/{attempts_left}): ").strip()
        if retry_pass == VALID_PASSWORD:
            print("Login successful.")
            return True
        else:
            remain = attempts_left - (i + 1)
            if remain > 0:
                print(f"Wrong password. You have {remain} chances left.")
            else:
                print("No more attempts.")
    forgot = input("Forgot password? (yes/no): ").strip().lower()
    if forgot == "yes":
        get_email = input("Enter your email Id: ").strip()
        if get_email.lower() != get_email:
            print("Email Id should be in lower case.")
            return False
        if get_email == VALID_EMAIL:
            print("Password reset flow would be here (simulated).")
            return False
        else:
            print("Wrong email Id.")
            return False
    return False

def display_categories():
    for i, name in enumerate(CATEGORIES.keys(), start=1):
        print(f"{i}. {name}")

def prompt_add_from_results(sample_item_name=None):
    ans = input("Would you like to add a product to the cart? (yes/no): ").strip().lower()
    if ans == "yes":
        if sample_item_name:
            use_sample = input(f"Add '{sample_item_name}'? (yes/no): ").strip().lower()
            if use_sample == "yes":
                add_to_cart(prefill_name=sample_item_name)
                return
        add_to_cart()

def browse_category():
    print("\n=== BROWSE CATEGORIES ===")
    display_categories()
    try:
        ch = int(input("Select category number to view: "))
        keys = list(CATEGORIES.keys())
        if 1 <= ch <= len(keys):
            selected_key = keys[ch-1]
            print_table(selected_key, CATEGORIES[selected_key])
            prompt_add_from_results()
        else:
            print("No such category found.")
    except ValueError:
        print("Please enter numbers only.")

def search_product(keyword):
    results = {item: details for item, details in products.items()
               if keyword.lower() in item.lower() or keyword.lower() in details[0].lower()}
    if results:
        print("\nSearch Results:")
        print_table("Search", results)
        sample = next(iter(results)) if len(results) == 1 else None
        prompt_add_from_results(sample_item_name=sample)
    else:
        print("No products found.")

def filter_products(filter_type, value):
    if filter_type == "price":
        results = {item: details for item, details in products.items() if details[1] <= value}
    elif filter_type == "product":
        results = {item: details for item, details in products.items() if value.lower() in item.lower()}
    elif filter_type == "company":
        results = {item: details for item, details in products.items() if value.lower() in details[0].lower()}
    else:
        print("Invalid filter type.")
        return
    if results:
        print_table("Filtered Results", results)
        sample = next(iter(results)) if len(results) == 1 else None
        prompt_add_from_results(sample_item_name=sample)
    else:
        print("No products match the filter.")

def add_to_cart(prefill_name=None):
    print("\n=== ADD TO CART ===")
    if prefill_name:
        name = prefill_name
        print(f"Selected product: {name}")
    else:
        name = input("Enter exact product name (as listed): ").strip()
    found = find_product_by_name(name)
    if not found:
        print("Product not found. Use browse or search to see available names.")
        return
    name, brand, price = found
    try:
        qty = int(input("Enter quantity: "))
        if qty <= 0:
            print("Quantity must be positive.")
            return
    except ValueError:
        print("Enter numbers only.")
        return
    for item in cart:
        if item["name"].lower() == name.lower():
            item["qty"] += qty
            print(f"Updated '{name}' quantity to {item['qty']}.")
            return
    cart.append({"name": name, "brand": brand, "price": price, "qty": qty})
    print(f"Added {qty} x {name} to cart.")

def view_cart():
    if not cart:
        print("\nCart is empty.")
        return
    print("\n=== CART ===")
    print(f"{'Item':30} {'Brand':20} {'Qty':5} {'Price':>8} {'Subtotal':>10}")
    print("-" * 80)
    total = 0
    for it in cart:
        subtotal = it["price"] * it["qty"]
        total += subtotal
        print(f"{it['name']:30} {it['brand']:20} {it['qty']:<5} ₹{it['price']:>7} ₹{subtotal:>9}")
    print("-" * 80)
    print(f"{'Total':>66} ₹{total}")
    ans = input("Would you like to remove an item from the cart? (yes/no): ").strip().lower()
    if ans == "yes":
        remove_from_cart()

def remove_from_cart():
    if not cart:
        print("\nCart is empty.")
        return
    name = input("Enter product name to remove (exact): ").strip()
    new_cart = [it for it in cart if it["name"].lower() != name.lower()]
    if len(new_cart) == len(cart):
        print("No such product in cart.")
    else:
        cart.clear()
        cart.extend(new_cart)
        print(f"Removed '{name}' from cart.")

def get_customer_details():
    print("\n--- CUSTOMER DETAILS ---")
    name = input("Enter Name: ").strip()
    address = input("Enter Address: ").strip()
    phone = input("Enter Phone Number: ").strip()
    return {"name": name, "address": address, "phone": phone}

def apply_discount(amount):
    print("\n--- DISCOUNT OPTIONS ---")
    print("1. New User - 10% OFF")
    print("2. Festival Offer - 15% OFF")
    print("3. No Discount")
    try:
        choice = int(input("Choose Discount (1-3): "))
    except ValueError:
        print("Invalid choice. No discount applied.")
        return amount
    if choice == 1:
        return amount * 0.90
    elif choice == 2:
        return amount * 0.85
    else:
        return amount

def process_payment(amount):
    print("\n--- PAYMENT METHOD ---")
    print("Payment Mode: Cash on Delivery")
    print(f"Amount Payable: ₹{amount:.2f}")
    return "Cash on Delivery"

def confirm_order():
    print("\n================ ORDER SUMMARY ================")
    for key, value in order.items():
        print(f"{key:<20}: {value}")
    print("================================================")
    choice = input("\nConfirm Order? (yes/no): ").strip().lower()
    if choice == "yes":
        print("\n🎉 ORDER CONFIRMED! 🎉")
    else:
        print("\n❌ ORDER CANCELLED BEFORE CONFIRMATION ❌")
        order.clear()

def cancel_order():
    if not order:
        print("\nNo active order to cancel.")
        return
    choice = input("Are you sure you want to CANCEL the order? (yes/no): ").strip().lower()
    if choice == "yes":
        order.clear()
        print("\n❌ ORDER CANCELLED SUCCESSFULLY ❌")
    else:
        print("\nOrder not cancelled.")

def place_order_flow():
    global order
    if not cart:
        print("\nCart is empty. Add items before placing an order.")
        return
    customer = get_customer_details()
    total = sum(it['price'] * it['qty'] for it in cart)
    total_after_discount = apply_discount(total)
    payment_mode = process_payment(total_after_discount)
    items_desc = ", ".join(f"{it['name']} x{it['qty']}" for it in cart)
    order = {
        "Customer Name": customer["name"],
        "Address": customer["address"],
        "Phone": customer["phone"],
        "Items": items_desc,
        "Total Bill": f"₹{total_after_discount:.2f}",
        "Payment Mode": payment_mode
    }
    confirm_order()
def main_menu():
    global CATEGORIES
    CATEGORIES = build_categories(products)  
    print("Welcome to the Online Shopping CLI Demo!")
    if not login():
        print("Login failed or skipped. You can still browse, but ordering requires login.")
    while True:
        print("\n======== MAIN MENU ========")
        print("1. Browse Categories")
        print("2. Search Product")
        print("3. Filter Products (price / product / company)")
        print("4. View Cart")
        print("5. Add to Cart")
        print("6. Remove from Cart")
        print("7. Place Order")
        print("8. Cancel Order")
        print("9. Exit")
        print("===========================")
        choice = input("Enter choice (1-9): ").strip()
        if choice == "1":
            browse_category()
        elif choice == "2":
            kw = input("Enter search keyword: ").strip()
            search_product(kw)
        elif choice == "3":
            typ = input("Filter by (price/product/company): ").strip().lower()
            if typ == "price":
                try:
                    val = int(input("Show products with price <= : "))
                    filter_products("price", val)
                except ValueError:
                    print("Enter a valid number.")
            else:
                val = input("Enter filter value: ").strip()
                filter_products(typ if typ in ("product","company") else "product", val)
        elif choice == "4":
            view_cart()
        elif choice == "5":
            add_to_cart()
        elif choice == "6":
            remove_from_cart()
        elif choice == "7":
            place_order_flow()
        elif choice == "8":
            cancel_order()
        elif choice == "9":
            print("Thank you for shopping with us! Goodbye.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main_menu()