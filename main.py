import csv
from pandas import DataFrame, merge, Series


#class to represent the products information
class Products:
	
	#constructor to load csv file into data frame and setup unit costs for products
	def __init__(self,csv_file):
		self.df_prod=DataFrame.from_csv("products.csv", index_col=False)
		
		#price_per_kg represent price of an item for one kg
		self.df_prod["price_per_kg"] = self.df_prod["Price"].divide(self.df_prod["Weight"])
		#if the weight of product is in grams convert its unit cost to kg equivalent
		for item, row in self.df_prod.iterrows():
			if row["Unit"]=="Grams":
				row["price_per_kg"]=row["price_per_kg"]*1000
				self.df_prod.set_value(item,"price_per_kg",row["price_per_kg"])

	#get list of all product names
	def get_products_names(self):
		return self.df_prod["Product Name"].unique().tolist()

	#get list of all product codes
	def get_products_codes(self):
		return self.df_prod["Product Code"].unique().tolist()

	#get list of all vendors for a particular product code
	def get_vendors(self,prod_code):
		return self.df_prod.loc[self.df_prod["Product Code"]==prod_code]["Vendor"].tolist()

	#get a list of cheapest prices of all products across all vendors
	def get_cheapest_prices(self):
		#group the rows by product codes, select the vendor giving minimum price within the group
		#min_idx stores index of such rows
		min_idx= self.df_prod.groupby(["Product Code"], sort=False)["price_per_kg"].transform(min) == self.df_prod["price_per_kg"]
		
		return self.df_prod[min_idx].values.tolist()

	#get a list of expensive prices of all products across all vendors
	def get_expensive_prices(self):
		#group the rows by product codes, select the vendor giving maximum price within the group
		#max_idx stores index of such rows
		max_idx= self.df_prod.groupby(["Product Code"], sort=False)["price_per_kg"].transform(max) == self.df_prod["price_per_kg"]
		
		return self.df_prod[max_idx].values.tolist()

	#get a list of cheapest prices of given products across all vendors
	def get_specific_prices(self,prod_codes):
		#group the rows by product codes, select the vendor giving minimum price within the group
		#min_idx stores index of such rows
		min_idx= self.df_prod.groupby(["Product Code"], sort=False)["price_per_kg"].transform(min) == self.df_prod["price_per_kg"]

		#select the rows for given product codes and store in result list
		result=[]
		for code in prod_codes:
			result.append(self.df_prod[min_idx].loc[self.df_prod["Product Code"]==code].values.tolist()[0])
		return result


#Class to store vendor information
class Vendors:
	
	#constructor to load csv file into data frame and setup unit costs for products
	def __init__(self,csv_file):
		self.df_prod=DataFrame.from_csv("products.csv", index_col=False)
		#price_per_kg represent price of an item for one kg
		self.df_prod["price_per_kg"] = self.df_prod["Price"].divide(self.df_prod["Weight"])
		#if the weight of product is in grams convert its unit cost to kg equivalent
		for item, row in self.df_prod.iterrows():
			if row["Unit"]=="Grams":
				row["price_per_kg"]=row["price_per_kg"]*1000
				self.df_prod.set_value(item,"price_per_kg",row["price_per_kg"])

	#get a list of all vendors
	def get_vendors_names(self):
		return self.df_prod["Vendor"].unique().tolist()

	#get a list of product sold by a given vendor
	def get_products(self,vendor_name):
		return self.df_prod.loc[self.df_prod["Vendor"]==vendor_name]["Product Name"].tolist()

	#get the prices of the cheapest product sold by each vendor
	def get_cheapest_products(self):
		#group the rows by product codes, select the vendor giving minimum price within the group
		#min_idx stores index of such rows
		min_idx= self.df_prod.groupby(["Vendor"], sort=False)["price_per_kg"].transform(min) == self.df_prod["price_per_kg"]
		
		return self.df_prod[min_idx].values.tolist()

	#get the prices of the expensive product sold by each vendor
	def get_expensive_products(self):
		#group the rows by product codes, select the vendor giving maximum price within the group
		#max_idx stores index of such rows
		max_idx= self.df_prod.groupby(["Vendor"], sort=False)["price_per_kg"].transform(max) == self.df_prod["price_per_kg"]
		
		return self.df_prod[max_idx].values.tolist()

def main():
	
	#instantiate a products using csv file
	products_inst=Products("products.csv")
	
	#print the cheapest prices of all products
	#the last value in each of the list represents price_per_kg, it has been added for comparison
	print "Cheapest Prices"
	print products_inst.get_cheapest_prices()
	print 
	#print expensive prices of all products
	print "Expensive Prices"
	print products_inst.get_expensive_prices()
	print 
	#print the cheapest prices of specific products
	print "Cheapest Prices of specific products"
	print products_inst.get_specific_prices([3736, 4356, 3732, 3746, 3759, 3719, 3740, 4341])


if __name__=="__main__":
	main()
