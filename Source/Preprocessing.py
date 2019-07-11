'''
Preprocessing.py
 Title: Data(instacart-market-basket-analysis/Kaggle) Preprocessing
Author: Lee SeokJune
'''
# import Library
import pandas as pd
#
class Preprocessing:
    def __init__(self):
        aisles = pd.read_csv('../Data/aisles.csv')
        departments = pd.read_csv('../Data/departments.csv')
        products = pd.read_csv('../Data/products.csv')
        orders = pd.read_csv('../Data/orders.csv')
        order_procucts_prior = pd.read_csv('../Data/order_products__prior.csv')
    def product(self, num = 0):
        
        if num != 0:
            
'''
# product
a1 = pd.read_csv('products.csv')
del a1['aisle_id']
a2 = pd.read_csv('departments.csv')

#print(a1)
#print(a2)

a = pd.merge(a1, a2, on = 'department_id', how = 'left')
del a['department_id']
a = pd.DataFrame(a, columns=['product_id', 'department', 'product_name'])
#print(a)
#a.to_csv('product.csv')
#############################
# order
t1 = pd.read_csv('orders.csv')
#print(t1)
t1 = t1[t1['eval_set'].isin(['prior'])]
#print(t1)
t2 = pd.read_csv('order_products__prior.csv')

t = pd.merge(t1, t2, on = 'order_id', how = 'outer')

del t['eval_set']
del t['order_number']
del t['order_dow']
del t['order_hour_of_day']
del t['days_since_prior_order']
del t['add_to_cart_order']
del t['reordered']
t = pd.DataFrame(t, columns=['order_id', 'user_id', 'product_id'])

#print(t)
#t.to_csv('order.csv')
#############################
# order + product
r = pd.merge(t, a, on = 'product_id', how = 'left')

print(r)
r.to_csv('result.csv')
'''
