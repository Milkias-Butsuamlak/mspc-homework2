"""
Product models for the shopping cart system.
"""
from ..constants import PRODUCT_TYPES
from datetime import datetime, timedelta

class Product:
    """Base class for all products."""
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display_info(self):
        print(f"{self.name} - ${self.price:}")

class Food(Product):
    """Food products with additional attributes."""
    def __init__(self, name, price, expiration_days, organic, calories):
        super().__init__(name, price)
        self.expiration_days = expiration_days
        self.organic = organic
        self.calories = calories
    def get_expiration_date(self):
        return datetime.now() + timedelta(days=self.expiration_days)
    def is_organic(self):
        return self.organic
    def get_calories(self):
        return self.calories

class Cleaning(Product):
    """Cleaning products with safety information."""
    def __init__(self, name, price, safe_for_children):
        super().__init__(name, price)
        self.safe_for_children = safe_for_children
    def is_safe_for_children(self):
        return self.safe_for_children
    
class Drink(Product):
    """Drink products with container and sugar information."""
    def __init__(self, name, price, expiration_days, sugar_content, container):
        super().__init__(name, price)
        self.expiration_days = expiration_days
        self.sugar_content = sugar_content
        self.container = container

    def get_expiration_date(self):
        return datetime.now() + timedelta(days=self.expiration_days)
    def get_sugar_content(self):
        return self.sugar_content
    def get_container_type(self):
        return self.container

def create_product(product_type, name):
    """Factory function to create products based on type and name.
    This function MUST return a Product object.
    """

    product_data = PRODUCT_TYPES[product_type][name]
    
    if product_type == 'food': 
        """"creating food object from class food"""        
        return Food(name, product_data["price"], product_data ["expiration_days"], 
                    product_data ["organic"], product_data ["calories"]) 
    elif product_type == 'cleaning':
        """"creating Cleaning object from class cleaning"""
        return Cleaning(name, product_data ["price"], product_data["safe_for_children"])
    elif product_type == 'drinks':
        """"creating drink object from class drink """
        return Drink(name, product_data["price"], product_data ["expiration_days"], product_data["sugar_content"], product_data["container"])