"""
Shopping cart model with user support and error handling.
"""
from ..decorators import membership_welcome
from ..constants import PRODUCT_TYPES, FIDELITY_POINTS
from typing import List, Dict, Union, Optional

class ShoppingCart:
    """Shopping cart with user support and error handling."""
    @membership_welcome # This is a decorator, I chose to record data here, you can change it if needed.
    def __init__(self, user: dict =None):
        self._items = {}  # Format: {product.name: {"product": product, "quantity": quantity}}
        self.user = user # This is new

    def add_product(self, product_type: str , product_name:str , quantity:Optional[Union[int,float]]=1):
        """Adds a product to the cart or increases its quantity."""
        try:
            # Try this
            ...
        except:
            # If it fails, print this
            print("Error adding product")

    def remove_product(self, product_name, quantity=1):
        """Removes a product from the cart or reduces its quantity."""
        try:
            ...
        except:
            print("Error removing product")

    def calculate_total(self):
        """Calculates the total cost of all items in the cart."""
        ...

    def display_cart(self):
        """Displays all items in the cart with their details."""
        
        print("\nShopping Cart:")
        
        for name, item in self._items.items(): # Don't forget to iterate over the items
           ... 
            # Display additional product information based on type
        
        print(f"\nTotal: ${self.calculate_total()}") 