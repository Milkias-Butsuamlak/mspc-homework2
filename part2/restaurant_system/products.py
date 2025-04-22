from .constants import CONSTANTS

class Burger:
    """Represents a single burger item with customizable toppings."""

    def __init__(self): # This is complete
        """Initializes a basic burger with no patty or cheese added yet."""
        self.patty = False
        self.cheese = False
        self.base_price = CONSTANTS['BURGUER_BASE_PRICE']

    def add_patty(self): # THis is missing    #done
        """Adds a patty to the burger."""
        self.patty = True
        print("Patty added...")

    def add_cheese(self): # This is missing   #done
        """Adds cheese to the burger."""
        self.cheese = True
        print("cheese added...")

    def get_price(self) -> float : # This is missing   #done
        """Calculates the total price of the burger based on added toppings."""
        total = self.base_price
        if self.patty: 
            total += CONSTANTS['ADDITIONAL_PATTY_PRICE']
        if self.cheese:
           total += CONSTANTS['ADDITIONAL_CHEESE_PRICE']
        return total

    def get_name(self)-> str:
        """Generates the display name for the burger based on added toppings."""
        if self.patty and self.cheese:  #if the burger has both patty and cheese
            burger_name = "cheeseburger"
        elif self.patty:        #if the burger just has patty
            burger_name= "burger"
        elif self.cheese:
            burger_name="vegan chesseburger" #if the burger just has cheese
        
        return burger_name

        
