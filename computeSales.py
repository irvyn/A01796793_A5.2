import json
import sys
import time
import os

def load_json(path):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except Exception as e:
        print(f"Could not load JSON file '{path}'. Details: {e}")
        return None

def build_price_map(catalogue):
    price_map = {}
    for item in catalogue:
        title = item.get("title")
        price = item.get("price")
        if title is not None and price is not None:
            price_map[title] = price
        else:
            print(f"Invalid product entry: {item}")
    return price_map

def compute_sales_total(sales, prices):
    total = 0.0
    lines = []

    for entry in sales:
        product = entry.get("Product")
        qty = entry.get("Quantity")
        sid = entry.get("SALE_ID")

        if product not in prices:
            lines.append(f"Product '{product}' not found in catalogue (SALE_ID: {sid})")
            print(f"Product '{product}' not found in catalogue (SALE_ID: {sid})")
            continue

        if not isinstance(qty, (int, float)):
            lines.append(f"Invalid quantity '{qty}' for '{product}' (SALE_ID: {sid})")
            print(f"Invalid quantity '{qty}' for '{product}' (SALE_ID: {sid})")
            continue

        price = prices[product]
        cost = price * qty
        total += cost
        lines.append(f"SALE_ID {sid} - {product} x{qty} = ${cost:.2f}")

    lines.append(f"TOTAL = ${total:.2f}")
    return total, "\n".join(lines)

def ensure_output_path(output_file_path):
    folder = os.path.dirname(output_file_path)
    if folder and not os.path.exists(folder):
        os.makedirs(folder, exist_ok=True)

catalogue_path = sys.argv[1]
sales_path = sys.argv[2]

start = time.time()

catalogue = load_json(catalogue_path)
sales = load_json(sales_path)

if catalogue is None or sales is None:
    print("Input files could not be loaded. Exiting...")
    sys.exit(1)

prices = build_price_map(catalogue)

total, text = compute_sales_total(sales, prices)

end = time.time()
elapsed = end - start

full_output = text + f"\nExecution time: {elapsed:.4f} seconds"

output_folder = os.path.dirname(sales_path)
output_file = os.path.join(output_folder, "SalesResults.txt")

ensure_output_path(output_file)

with open(output_file, "w") as f:
    f.write(full_output)

print(full_output)