# SuperPy Report

Explaination of some technical choices.

## Buy and Sell

Both the `buy` and `sell` functions take multiple arguments of a specifict format in order to write data to a csv.
```
    while True:
        try:
            amount = int(input('Amount of items bought: '))
            break
        except:
            print('Please try again with a whole number, example: 5')
```

In this code example you can see how i decided to solve this problem, by wrapping the `try` `except` in a `while True` loop, the program will keep asking for input until a valid input das been given.

## Inventory functions

In the `inventory.py` file i decided to write all the functions in small seperate steps, so parts can be easily reused.

for example:
```
def get_bought_items():
    # Reads the bought.csv file and returns a list of dictionaries containing all bought items.
```

is used later in:

```
def get_available_products():
    # Compares the bough and sold products and expiration dates and returns available products
    bought_items = get_bought_items()
    sold_ids = get_sold_ids()
    available_products = []
    today = get_date()
    for item in bought_items:
        if item['id'] not in sold_ids and item['expiration_date'] >= today:
            available_products.append(item)
    return available_products
```

and also:

```
    def get_expired_products():
    # Compares the bough and sold products and expiration dates and returns expired products
    bought_items = get_bought_items()
    sold_ids = get_sold_ids()
    expired_products = []
    today = get_date()
    for item in bought_items:
        if item['id'] not in sold_ids and item['expiration_date'] < today:
            expired_products.append(item)
    return expired_products
```
