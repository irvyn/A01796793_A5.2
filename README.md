# Activity 5.2 - Programming Exercise 2: Compute Sales

This project is a Python-based tool designed to calculate total sales costs by processing product catalogues and sales records provided in JSON format. The development focuses on **clean code**, **static analysis compliance**, and **efficient data processing**.

## 📋 Description

The program processes two input files:
1.  **Price Catalogue**: A JSON file containing product titles and their respective prices.
2.  **Sales Record**: A JSON file containing details of sales (Product name, Quantity, and Sale ID).

The script computes the total for each valid sale, handles errors (missing products or invalid data), and generates a human-readable report both on the console and in a file named `SalesResults.txt`.

## 🚀 Requirements

According to the activity guidelines:
* **Req 1**: Invoked via command line with two file parameters.
* **Req 2**: Compute total cost, output to screen and `SalesResults.txt`.
* **Req 3**: Handle invalid data and continue execution.
* **Req 4**: Script named `compute_sales.py` (following snake_case for PEP 8).
* **Req 5**: Usage format: `python compute_sales.py priceCatalogue.json salesRecord.json`.
* **Req 6**: Manage data scale from hundreds to thousands of items.
* **Req 7**: Display and record execution time.
* **Req 8**: **PEP 8 Compliance**.

## 🛠️ Static Analysis

To ensure code quality, the following tools were used:
- **Pylint**: Achieved a score of **10/10**.
- **Flake8**: 0 errors (fully compliant with PEP 8 length and formatting rules).

Evidence of these results can be found in the `TCX/` folders or the evidence screenshots.

## 💻 Usage

Run the script from your terminal using the following command:

```bash
python compute_sales.py <path_to_catalogue.json> <path_to_sales.json>
