# Imports
import argparse
from date import advance_date, print_date, set_date_today
from buy import buy_item
from sell import sell_item
from inventory import display_inventory, display_purchases, display_sales
import revenue


# Do not change these lines.
__winc_id__ = 'a2bc36ea784242e4989deb157d527ba0'
__human_name__ = 'superpy'


# Your code below this line.

parser = argparse.ArgumentParser(
    description="Handle the supermarket's inventory.")
subparser = parser.add_subparsers(dest='command', required=True)

# Date parsers
advance_date_parser = subparser.add_parser(
    'advancedate', help="Advance the date a number of days.")
advance_date_parser.set_defaults(func=advance_date)
show_date_parser = subparser.add_parser(
    'showdate', help="Show the system date.")
show_date_parser.set_defaults(func=print_date)
set_today_parser = subparser.add_parser(
    'settoday', help="Set the system date to the current date.")
set_today_parser.set_defaults(func=set_date_today)

# revenue parsers
total_revenue_parser = subparser.add_parser(
    'totalrevenue', help="Show the total revenue, between now and the beginning of time.")
total_revenue_parser.set_defaults(func=revenue.print_total_revenue)
date_revenue_parser = subparser.add_parser(
    'daterevenue', help="Show the total revenue, between between two dates.")
date_revenue_parser.set_defaults(func=revenue.print_revenue_between_dates)

# Sales parsers
buy_parser = subparser.add_parser(
    'buy', help="Register the purchasing of a product.")
buy_parser.set_defaults(func=buy_item)
sell_parser = subparser.add_parser(
    'sell', help="Register a sale.")
sell_parser.set_defaults(func=sell_item)

# Inventory parsers
inventory_parser = subparser.add_parser(
    'inventory', help="Shows the amounts of currently available products.")
inventory_parser.set_defaults(func=display_inventory)
sales_parser = subparser.add_parser(
    'sales', help="Shows all sales made since the beginning of time.")
sales_parser.set_defaults(func=display_sales)
purchases_parser = subparser.add_parser(
    'purchases', help="Shows all purchases made since the dawn of man.")
purchases_parser.set_defaults(func=display_purchases)


args = parser.parse_args()


def main():
    args.func()


if __name__ == '__main__':
    main()
