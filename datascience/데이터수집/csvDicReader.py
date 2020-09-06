import csv

with open('colon_delimited_stock_prices.txt') as f:

    tab_reader = csv.DictReader(f, delimiter=':')

    for row in tab_reader:
        date = row["date"]
        symbol = row["symbol"]
        closing_price = float(row["closing_price"])

        print(date, symbol, closing_price)