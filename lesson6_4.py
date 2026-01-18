# --- Setup Variables ---
item_price = 15.50  # A float
quantity = 2        # An integer
user_greeting = "Welcome, "
user_name = "AI PRO"

# --- 1. Arithmetic Operators ---
# Let's calculate the total cost
total_cost = item_price * quantity
print(f"Total Cost: {total_cost}")

# --- 2. String Concatenation ---
# Let's create a welcome message
welcome_message = user_greeting + user_name
print(f"Message: {welcome_message}")

# --- 3. Comparison Operators ---
# Let's check if the cost is exactly 31.0
is_cost_31 = (total_cost == 31.0)
print(f"Is the cost exactly 31.0? {is_cost_31}")

# --- 4. Logical Operators ---
# Let's see if a customer gets a special offer.
# They need to buy more than 1 item AND the total cost must be under $50
gets_offer = (quantity > 1) and (total_cost < 50.0)
print(f"Customer gets special offer? {gets_offer}")
