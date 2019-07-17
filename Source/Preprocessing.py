'''
Preprocessing.py
 Title: Data(instacart-market-basket-analysis/Kaggle) Preprocessing
'''
# import Library
import pandas as pd
import numpy as np

class Preprocessing:
    # Load Data(.csv File)
    def __init__(self):
        self.aisles = pd.read_csv('../Data/aisles.csv')
        self.departments = pd.read_csv('../Data/departments.csv')
        self.products = pd.read_csv('../Data/products.csv')
        self.orders = pd.read_csv('../Data/orders.csv')
        self.orders = self.orders[self.orders['eval_set'].isin(['prior'])]
        self.order_products_prior = pd.read_csv('../Data/order_products__prior.csv')
        
    # Add Price to Products
    def priceToProducts(self):
        self.products = pd.merge(self.products,
                                 pd.DataFrame((np.random.rand(self.products['product_id'].count()) * 10).round(2), columns = ['price']),
                                 left_index = True, right_index = True, how = 'left')
            
    # Products + (aisles & departments)
    def extendProducts(self, num):
        self.eproducts = pd.merge(self.products, self.aisles, on = 'aisle_id', how = 'left')
        self.eproducts = pd.merge(self.eproducts, self.departments, on = 'department_id', how = 'left')
        self.eproducts = pd.DataFrame(self.eproducts, columns=['product_id', 'product_name',
                                                               'department_id', 'department',
                                                               'aisle_id', 'aisle'])
        # Save Data(Extend Products)
        if num == 0:
            self.eproducts.to_csv('../PreprocessData/ExtendProducts.csv', index = False)
            
    # Orders + (order_products_prior)
    def extendOrders(self, num):
        self.eorders = pd.merge(self.orders[self.orders['eval_set'].isin(['prior'])], self.order_products_prior, on = 'order_id', how = 'outer')
        self.eorders = pd.DataFrame(self.eorders, columns=['order_id', 'product_id',
                                                           'user_id', 'eval_set', 'order_number', 'order_number', 'order_dow', 'order_hour_of_day', 'days_since_prior_order',
                                                           'add_to_cart_order', 'reordered'])
        # Delete Unnecessary Columns
        '''
        # orders
        del self.eorders['eval_set']
        del self.eorders['order_number']
        del self.eorders['order_dow']
        del self.eorders['order_hour_of_day']
        del self.eorders['days_since_prior_order']
        # order_products_prior
        del self.eorders['add_to_cart_order']
        del self.eorders['reordered']
        '''
        # Save Data(Extend Orders)
        if num == 0:
            self.eorders.to_csv('../PreprocessData/ExtendOrders.csv', index = False)

    # ExtendOrders + (ExtendProducts)
    def totalOrders(self, num):
        self.torders = pd.merge(self.eorders, self.eproducts, on = 'product_id', how = 'left')
        # Save Data(Total Orders)
        if num == 0:
            self.torders.to_csv('../PreprocessData/TotalOrders.csv', index = False)
         
     # Get Sampling TotalOrders csv file 
    def getSampleCSV(self):
        self.torders_ = pd.read_csv('../PreprocessData/TotalOrders_.csv')

    # Run Preprocessing
    def run(self, num = -1):
        if num == 1:
            self.getSampleCSV()
            return self.torders_
        else:
            self.priceToProducts()
            self.extendProducts(num)
            self.extendOrders(num)
            self.totalOrders(num)
            return self.torders
