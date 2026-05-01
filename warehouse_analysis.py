
# --- STEP 1: VARIABLES & DATA TYPES ---

# We are defining the first row from your Excel
item_category = "Electronics"  # String (Metin)
item_stock = 450               # Integer (Tam Sayı)
item_critical_level = 500      # Integer (Kritik Seviye)
item_unit_cost = 120.50        # Float (Ondalıklı Sayı)

# Let's check if the stock is low using an OPERATOR
is_low_stock = item_stock < item_critical_level  # Boolean (True/False)

print(f"Product: {item_category}")
print(f"Is stock low? {is_low_stock}")
# --- STEP 2: ORGANIZING DATA (LIST & DICTIONARIES) ---

# We put every row into a 'Dictionary' and then into a 'List'
inventory_list = [
    {"category": "Electronics", "stock": 450, "limit": 500},
    {"category": "Textiles", "stock": 800, "limit": 300},
    {"category": "Food", "stock": 200, "limit": 300},
    {"category": "Chemicals", "stock": 150, "limit": 100}
]
# --- STEP 3: AUTOMATION (LOOPS & IF CONDITIONS) ---

print("\n--- INVENTORY STATUS REPORT ---")

# Python will take each 'product' from 'inventory_list' one by one
for product in inventory_list:
    name = product["category"]
    current_stock = product["stock"]
    threshold = product["limit"]

    # Logic: If stock is less than the limit, give a warning
    if current_stock < threshold:
        status = "⚠️ ORDER NOW!"
    else:
        status = "✅ STOCK OK"

    print(f"Department: {name:12} | Status: {status}")
import matplotlib.pyplot as plt

# --- PREPARING DATA FOR THE GRAPH ---
# We need to extract names and stocks into separate lists for the chart
product_names = [p["category"] for p in inventory_list]
stock_values = [p["stock"] for p in inventory_list]
limit_values = [p["limit"] for p in inventory_list]

# --- CREATING THE PLOT ---
plt.figure(figsize=(10, 6)) # Chart size

# Bar chart for current stocks
plt.bar(product_names, stock_values, color='skyblue', label='Current Stock')

# A red line for the critical threshold (To see who is below the limit)
plt.axhline(y=300, color='red', linestyle='--', label='Average Safety Limit')

# --- CUSTOMIZING THE GRAPH (Professional Touch) ---
plt.title('Inventory Status Analysis - May 2026', fontsize=15)
plt.xlabel('Departments', fontsize=12)
plt.ylabel('Quantity', fontsize=12)
plt.legend() # Shows what colors mean
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show the final result
plt.show()

 Product: Electronics
Is stock low? True

--- INVENTORY STATUS REPORT ---
Department: Electronics  | Status: ⚠️ ORDER NOW!
Department: Textiles     | Status: ✅ STOCK OK
Department: Food         | Status: ⚠️ ORDER NOW!
Department: Chemicals    | Status: ✅ STOCK OK
