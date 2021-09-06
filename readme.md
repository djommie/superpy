# SuperPy

Supermarket inventory system using command line arguments

## Modules

-   argparse (https://docs.python.org/3/library/argparse.html)
-   csv (https://docs.python.org/3/library/csv.html)
-   datetime (https://docs.python.org/3/library/datetime.html)
-   rich (https://rich.readthedocs.io/en/stable/introduction.html)


## Commandline Options

example:

python main.py buy

positional arguments:

  -h, --help          Shows the help message and exits the program
  showdate            Shows the system's date
  advancedate         Advances the system's date by a given number of days
  settoday            Sets the system's date to today's date
  totalrevenue        Shows the total revenue since the start of the date  
  daterevenue         Shows the revenue between two given dates
  buy                 Starts the buy registration process
  sell                Starts the sale registration process
  inventory           Shows the current products and their number of stocks
  sales               Reports on all sales made
  purchases           Reports on all purchases made
```

Asks for two dates, earliest first and latest second in 'YYYY-MM-DD' format and shows the revenue between these dates

### `showdate`

Shows the date currently maintained by the system, saved in date.txt (note: system date is not necessarily today's date)

-   `python ./main.py buy --product-name orange --price 0.8 --expiration-date 2020-05-01`

### `advancedate`

Asks for an integer and advances the system date by this many days by writing the new date to date.txt

-   `python ./main.py advancedate`

### `settoday`

Uses datetime to get today's date and writes this date to date.txt

-   `python ./main.py settoday`

### `totalrevenue`

Reads all the sales prices from `sales.csv` and shows the total 

-   `python ./main.py totalrevenue`

### `daterevenue`

Same as total revenue, but asks for two dates, earliest first and latest second, in 'YYYY-MM-DD' format and returns the total revnue between the given dates

-   `python ./main.py daterevenue`

### `buy`

Starts the buy registration process, asks for a product name, amount(int), the price(float, accepts int), number of days from now the product will expire (int) and writes the bought item(s) to the `bought.csv` file 

-   `python ./main.py buy`

### `sell`

Starts the sales registration process, asks for a product name and number of items and checks if these are available, asks for sell price and writes the sold products to sales.csv 

-   `python ./main.py sell`

### `inventory`

Checks which items are currently available and uses Rich to report the numbers

-   `python ./main.py inventory`

### `sales`

Reads `sales.csv` and reports all the relevant information using a Rich Table 

-   `python ./main.py sales`

### `purchases` 

reads `bought.csv` and reports all the relevant information using a Rich Table

-   `python ./main.py purchases`
