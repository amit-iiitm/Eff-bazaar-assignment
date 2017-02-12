# Eff-bazaar-assignment
#Introduction
The project deals with getting vital prices information of products such as cheapest prices, expensive prices from given data file.
The file "products.csv" contains information about products and their vendors.

main.py --> Main file that contains two classes: one for storing products information(Products), and other for storing vendors information(Vendors). These classes have few methods to deal with raw data and give information such as vendors list, products list, Cheapest prices, Expensive prices and cheapest prices for a specific product. 

test_main.py--> Testing the product class functions by unit testing and reference output of those functions.

#Requirements
This project is built in Python-2.7.9 version.
The modules required to run this project has been specified in 'requirements.txt'.
Kindly install them "pip install -r requirements.txt" before testing this.

#Testing this project
Run the file "main.py"
This will print 3 lists:
List of cheapest prices
List of Expensive prices
List of cheapest prices for specific products [3736, 4356, 3732, 3746, 3759, 3719, 3740, 4341]

To run the test :
Run the file "test_main.py"
