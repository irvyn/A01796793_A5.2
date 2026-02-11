"""
Module for calculating sales based on JSON files.
"""

import json
import sys
import time
import os


def load_json(path):
    """Load a JSON file and handle potential reading errors."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: File not found at '{path}'.")
    except json.JSONDecodeError:
        print(f"Error: File '{path}' is not a valid JSON.")
    except Exception as e:  # pylint: disable=broad-except
        print(f"Unexpected error while loading '{path}': {e}")
    return None


def build_price_map(catalogue):
    """Create a price mapping dictionary from the catalogue data."""
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
    """Compute total sales and generate a detailed string report."""
    total = 0.0
    lines = []

    for entry in sales:
        product = entry.get("Product")
        qty = entry.get("Quantity")
        sid = entry.get("SALE_ID")

        if product not in prices:
            msg = f"Product '{product}' not found in catalogue (ID: {sid})"
            lines.append(msg)
            print(msg)
            continue

        if not isinstance(qty, (int, float)):
            msg = f"Invalid quantity '{qty}' for product '{product}' (ID: {sid})"
            lines.append(msg)
            print(msg)
            continue

        cost = prices[product] * qty
        total += cost
        lines.append(f"SALE_ID {sid} - {product} x{qty} = ${cost:.2f}")

    lines.append(f"TOTAL = ${total:.2f}")
    return total, "\n".join(lines)


def ensure_output_path(output_file_path):
    """Ensure that the output directory exists."""
    folder = os.path.dirname(output_file_path)
    if folder and not os.path.exists(folder):
        os.makedirs(folder, exist_ok=True)


def main():
    """Main function to coordinate the script execution."""
    if len(sys.argv) < 3:
        print("Usage: python script.py catalogue.json sales.json")
        sys.exit(1)

    catalogue_path = sys.argv[1]
    sales_path = sys.argv[2]

    start_time = time.time()

    catalogue = load_json(catalogue_path)
    sales = load_json(sales_path)

    if catalogue is None or sales is None:
        print("Input files could not be loaded. Exiting...")
        sys.exit(1)

    prices = build_price_map(catalogue)
    _, text = compute_sales_total(sales, prices)

    elapsed = time.time() - start_time
    full_output = f"{text}\nExecution time: {elapsed:.4f} seconds"

    output_folder = os.path.dirname(sales_path)
    output_file = os.path.join(output_folder, "SalesResults.txt")

    ensure_output_path(output_file)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(full_output)

    print(full_output)


if __name__ == "__main__":
    main()
