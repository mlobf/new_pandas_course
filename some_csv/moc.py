import pandas as pd

# ok
# csv = 'heart.csv'

# ok
csv = 'PRICES-STOCK.csv'

# ok => Just use | as delimiter
csv = 'PRODUCTS.csv'

products = pd.read_csv(csv, delimiter='|')
print(products)
