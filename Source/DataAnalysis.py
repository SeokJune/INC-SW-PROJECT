'''
DataAnalysis.py

'''

# import Library
import pandas as pd
import matplotlib.pyplot as plt


class DataAnalysis:
    
    # Load Data(.csv file)
    def ReadData(self):
        self.torders_ = pd.read_csv('../PreprocessData/TotalOrders_.csv')
        self.department = pd.read_csv('../Data/departments.csv')
        self.Product = pd.read_csv('../Data/products.csv')
        del self.Product['aisle_id']
        del self.Product['department_id']

    # Binding Data to Parameter   
    def BindingData(self):
        self.ProductDep = self.torders_['department']
        self.ProductId = self.torders_['product_id']
        self.ProductIdCount = self.ProductId.value_counts().head(15)
        self.ReProduct = self.torders_[self.torders_['reordered'].isin(['1'])].loc[:,['product_id']]['product_id']
        self.ReProductIdCount = self.ReProduct.value_counts().head(15)

    # Showing Best Products graph     
    def BestProducts(self, key):
        self.ProductIdCountDF = pd.DataFrame({'product_id':self.ProductIdCount.index, 'product_count':self.ProductIdCount.values})
        self.mergeDF = pd.merge(self.ProductIdCountDF,self.Product)
        self.mergeDF.sort_values(by='product_count',ascending=True).plot(kind='barh',
                                                                     x='product_name',y='product_count',
                                                                     title = 'Best Products',grid=True)
        plt.xlabel('ProductName')
        plt.ylabel('SalesRate')
        plt.subplots_adjust(left=0.17)
        plt.get_current_fig_manager().window.state('zoomed')
        plt.show()
        
    # Showing Best Department graph
    def BestDepartment(self, key):
        self.ProductDepCount = self.ProductDep.value_counts()
        self.ProductDepCount.sort_values().plot(kind='barh',figsize=(10,6), title='Best Department', grid=True)
        
        plt.xlabel('SalesRate')
        plt.ylabel('Department')
        plt.subplots_adjust(left=0.17)
        plt.get_current_fig_manager().window.state('zoomed')
        plt.show()
        
    # Showing Best Reordered Products graph
    def BestReorderedProducts(self, key):
        self.ReProductIdCountDF = pd.DataFrame({'product_id':self.ReProductIdCount.index, 'reproduct_count':self.ReProductIdCount.values})
        self.mergeDF = pd.merge(self.ReProductIdCountDF,self.Product)
        self.mergeDF.sort_values(by='reproduct_count',ascending=True).plot(kind='barh',
                                                       x='product_name', y='reproduct_count',
                                                       title='Best Reordered Products',grid=True)
        plt.xlabel('ReorderRate')
        plt.ylabel('ProductName')
        plt.subplots_adjust(left=0.17)
        plt.get_current_fig_manager().window.state('zoomed')
        plt.show()

    # Relationship between the Best Products and the Best Reordered Products    
    def BestProducts_Reodered(self, key):
        self.ProductIdCountDF = pd.DataFrame({'product_id':self.ProductIdCount.index, 'product_count':self.ProductIdCount.values})
        self.ReProductIdCountDF = pd.DataFrame({'product_id':self.ReProductIdCount.index, 'reproduct_count':self.ReProductIdCount.values})
        self.mergeDF = pd.merge(self.ProductIdCountDF,self.ReProductIdCountDF)
        self.mergeDF = pd.merge(self.mergeDF,self.Product)
        self.mergeDF.sort_values(by='product_count',ascending=True).plot(kind='barh',
                                                       x='product_name', y=['reproduct_count','product_count'], 
                                                       figsize=(8,8),
                                                       title='Total Product Sales Rate',grid=True)
        plt.xlabel('SalesRate')
        plt.ylabel('ProductName')
        plt.subplots_adjust(left=0.17)
        plt.get_current_fig_manager().window.state('zoomed')
        plt.show()

    # Popular Products by Product category
    def ProductsByCategory(self, key):
        self.dep2 = self.department.set_index('department_id')
        print(self.dep2)
        self.cat = int(input('choose category: '))
    
        self.selproductId = self.torders_[self.torders_['department_id'].isin([str(self.cat)])].loc[:,['product_id']]['product_id']
        self.selproductIdCount = self.selproductId.value_counts().head(15)
        self.selproductIdCountDF = pd.DataFrame({'product_id':self.selproductIdCount.index, 'product_count':self.selproductIdCount.values})
    
        self.mergeDF = pd.merge(self.selproductIdCountDF,self.Product)
        self.selproductName = self.department[self.department['department_id'] == self.cat]['department']
        self.seltitle = 'Best ' + self.selproductName[self.cat-1] + ' Products'
        self.mergeDF.sort_values(by='product_count',ascending=True).plot(kind='barh',
                                                                     x='product_name',y='product_count',
                                                                     figsize=(8,8),
                                                                     title=self.seltitle,
                                                                     grid=True) # self.de[self.de[''] == 3]['name']
        plt.xlabel('SalesRate')
        plt.ylabel('ProductName')
        plt.subplots_adjust(left=0.17)
        plt.get_current_fig_manager().window.state('zoomed')
        plt.show()
        
    # Run main Program
    def run(self):
        self.ReadData()
        self.BindingData()
        while(1):
            print('Best Products ▶ 1'+'\n'+
                  'Best Department ▶ 2'+'\n'+
                  'Best Reordered Products ▶ 3'+'\n'+
                  'Best Products and Reodered Products ▶ 4'+'\n'+
                  'Popular Products by Department ▶ 5'+'\n'+
                  'Quit ▶ 6')
            print('\n')
            self.key = int(input('Choose the data you want:'))
            print('\n')
        
            if self.key == 1:
                self.BestProducts(self.key)
            elif self.key == 2:
                self.BestDepartment(self.key)
            elif self.key == 3:
                self.BestReorderedProducts(self.key)
            elif self.key == 4:
                self.BestProducts_Reodered(self.key)
            elif self.key == 5:
                self.ProductsByCategory(self.key)
            elif self.key == 6:
                break
            else:
                #error return
                print('error')
                break
                
