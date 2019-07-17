'''
import Preprocessing
prepro = Preprocessing.Preprocessing()

'''
import pandas as pd
import matplotlib.pyplot as plt

class DataAnalysis:
    
    def __init__(self):
        self.torders_ = pd.read_csv('Data/TotalOrders_.csv')
        self.Product = pd.read_csv('Data/products.csv')
        del self.Product['aisle_id']
        del self.Product['department_id']
        
    def BestProducts(self, key):
        self.ProductId = self.torders_['product_id']
        self.ProductIdCount = self.ProductId.value_counts().head(15)
        self.ProductIdCount.plot(kind='bar',figsize=(10,6), title='Best Product')
        plt.xlabel('ProductID')
        plt.ylabel('SalesRate')
        plt.show()
        
    def BestDepartment(self, key):
        self.ProductDep = self.torders_['department']
        self.ProductDepCount = self.ProductDep.value_counts()
        self.ProductDepCount.sort_values().plot(kind='barh',figsize=(10,6), title='Best Department', grid=True)
        plt.xlabel('SalesRate')
        plt.ylabel('Department')
        plt.show()
        
    def BestReorderedProducts(self, key):
        self.ReProduct = self.torders_[self.torders_['reordered'].isin(['1'])].loc[:,['product_id']]['product_id']
        self.ReProductCount = self.ReProduct.value_counts().head(15)
        self.ReProductCount.plot(kind='bar',figsize=(10,6), title='Best Reorder Product')
        plt.xlabel('ProductID')
        plt.ylabel('ReorderRate')
        plt.show()
        
    def BestProducts_Reodered(self, key):
        self.ProductIdCountDF = pd.DataFrame({'product_id':self.ProductIdCount.index, 'product_count':self.ProductIdCount.values})
        self.ReProductCountDF = pd.DataFrame({'product_id':self.ReProductCount.index, 'reproduct_count':self.ReProductCount.values})
        self.mergeDF = pd.merge(self.ProductIdCountDF,self.ReProductCountDF)
        self.mergeDF = pd.merge(self.mergeDF,self.Product)
        self.mergeDF.sort_values(by='product_count',ascending=True).plot(kind='barh',
                                                       x='product_name', y=['reproduct_count','product_count'], 
                                                       figsize=(8,8),
                                                       title='Total Product Sales Rate',grid=True)
        plt.show()
        
    def run(self):
        print('Best Products ▶ 1'+'\n'+'Best Department ▶ 2'+'\n'+'Best Reordered Products ▶ 3' +
              '\n'+'Best Products and Reodered Products ▶ 4')
        self.key = int(input('Choose the data you want:'))
        
        if self.key == 1:   
            self.BestProducts(self.key)
        elif self.key == 2:
            self.BestDepartment(self.key)
        elif self.key == 3:
            self.BestReorderedProducts(self.key)
        elif self.key == 4:
            self.BestProducts_Reodered(self.key)
        else:
            print('error')
            #error return
