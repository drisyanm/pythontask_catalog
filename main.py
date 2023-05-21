# Product catalog
products = {
    "Product A": 20,
    "Product B": 40,
    "Product C": 50
}

# Discount rules
discount_rules = {
    "flat_10_discount": {"threshold": 200, "discount_amount": 10},
    "bulk_5_discount": {"threshold": 10, "discount_percentage": 5},
    "bulk_10_discount": {"threshold": 20, "discount_percentage": 10},
    "tiered_50_discount": {"quantity_threshold": 30, "single_product_threshold": 15, "discount_percentage": 50}
}

# Fees
gift_wrap_fee = 1
shipping_fee_per_package = 5
products_per_package = 10

# Function to calculate the discount amount based on discount rule
def calculate_discount(rule, total_quantity, single_product_quantity, total_price):
    discount = 0

    if rule == "flat_10_discount" and total_price > discount_rules[rule]["threshold"]:
        discount = discount_rules[rule]["discount_amount"]
    elif rule == "bulk_5_discount" and single_product_quantity > discount_rules[rule]["threshold"]:
        discount = total_price * discount_rules[rule]["discount_percentage"] / 100
    elif rule == "bulk_10_discount" and total_quantity > discount_rules[rule]["threshold"]:
        discount = total_price * discount_rules[rule]["discount_percentage"] / 100
    elif rule == "tiered_50_discount" and total_quantity > discount_rules[rule]["quantity_threshold"] and single_product_quantity > discount_rules[rule]["single_product_threshold"]:
        discount = (single_product_quantity - discount_rules[rule]["single_product_threshold"]) * products[item] * discount_rules[rule]["discount_percentage"] / 100

    return discount

# Function to calculate the total amount for each product
def calculate_product_total(quantity, price):
    return quantity * price

# Function to calculate the total shipping fee
def calculate_shipping_fee(total_quantity):
    return (total_quantity // products_per_package) * shipping_fee_per_package

# Function to calculate the total amount for gift wrapping
def calculate_gift_wrap_fee(quantity):
    return quantity * gift_wrap_fee

# Main program
cart = {}
total_quantity = 0
subtotal = 0

# Input the quantity and gift wrap information for each product
for item, price in products.items():
    quantity = int(input(f"Enter the quantity of {item}: "))
    is_gift_wrapped = input(f"Is {item} wrapped as a gift? (y/n): ")

    cart[item] = {
        "quantity": quantity,
        "price": price,
        "is_gift_wrapped": is_gift_wrapped.lower() == "y"
    }

    total_quantity += quantity
    subtotal += calculate_product_total(quantity, price)

discount_applied = False
discount_name = ""
discount_amount = 0

# Apply the most beneficial discount
for rule in discount_rules.keys():
    discount = calculate_discount(rule, total_quantity, max(cart[item]["quantity"] for item in cart), subtotal)
    if discount > discount_amount:
        discount_name = rule
        discount_amount = discount
        discount_applied = True

gift_wrap_total = sum(calculate_gift_wrap_fee(cart[item]["quantity"]) for item in cart if cart[item]["is_gift_wrapped"])
shipping_fee_total = calculate_shipping_fee(total_quantity)

total = subtotal - discount_amount + gift_wrap_total + shipping_fee_total

# Output the order details
print("\n==== Order Details ====")
for item in cart:
    print(f"{item}: Quantity: {cart[item]['quantity']}, Total Amount: ${calculate_product_total(cart[item]['quantity'], cart[item]['price'])}")

print(f"Subtotal: ${subtotal}")

if discount_applied:
    print(f"Discount Applied: {discount_name}, Amount: ${discount_amount}")

print(f"Gift Wrap Fee: ${gift_wrap_total}")
print(f"Shipping Fee: ${shipping_fee_total}")
print(f"Total: ${total}")


