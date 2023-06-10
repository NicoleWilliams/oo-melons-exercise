"""Classes for melon orders."""

class AbstractMelonOrder:
    """An abstract class to hold repetitive code"""
    base_price = 5
    shipped = False

    def __init__(self,species,qty):
        self.species = species
        self.qty = qty
        # self.tax = tax 
    
    def mark_shipped(self):
        """Record the fact than an order has been shipped."""
        self.shipped = True

    def get_total(self):
        """Calculate price, including tax."""
        if self.species == 'christmas melons':
            self.base_price = self.base_price*1.5
            
        total = (1 + self.tax) * self.qty * self.base_price

        if self.qty < 10 and self.order_type == 'international':
            total = total +3
            
        return total 
    
    def __repr__(self):
        return f'Species: {self.species}, Qty: {self.qty}, Tax: {self.tax}'

class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    tax = 0.08
    order_type = "domestic"

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        # self.shipped = False
        # self.order_type = "domestic"
        # self.tax = 0.08

    # def get_total(self):
    #     """Calculate price, including tax."""

    #     base_price = 5
    #     total = (1 + self.tax) * self.qty * self.base_price

    #     return total

    # def mark_shipped(self):
    #     """Record the fact than an order has been shipped."""

    #     self.shipped = True


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    tax = 0.17
    order_type = "international"

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.country_code = country_code
        # self.shipped = False
        # self.order_type = "international"
        # self.tax = 0.17

    # def get_total(self):
    #     """Calculate price, including tax."""

    #     base_price = 5
    #     total = (1 + self.tax) * self.qty * base_price

    #     return total

    # def mark_shipped(self):
    #     """Record the fact than an order has been shipped."""

    #     self.shipped = True

    def get_country_code(self):
        """Return the country code."""

        return self.country_code
