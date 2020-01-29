import pandas as pd

products = pd.DataFrame ([
    {'Price' : 5.0, 'Product' : 'Sushi Roll', 'Product ID': 4109},
    {'Price' : 0.5, 'Product' : 'Egg', 'Product ID': 1412},
    {'Price' : 1.5, 'Product' : 'Begel', 'Product ID': 8931}
    ])

products = products.set_index('Product ID')

invoices = pd.DataFrame([
    {'Customer':'Ali', 'Product ID':4109, 'Quantity':1},
    {'Customer':'Eric', 'Product ID':1412, 'Quantity':12},
    {'Customer':'Ande', 'Product ID':8931, 'Quantity':6},
    {'Customer':'Sam', 'Product ID':4109, 'Quantity':2}
    ])

print(products)
print()
print(invoices)
print('After Join')
print(pd.merge(products,invoices, how = 'outer', left_index = True, right_on = 'Product ID'))
