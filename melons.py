"""This file should have our order classes in it."""

class AbstractMelonOrder(object):
    """ Parent class for various types of melon orders. """

    def __init__(self, species, qty, order_type, tax):
        """ Initialize all melon order types. """

        self.species = species
        self.qty = qty
        self.order_type = order_type
        self.tax = tax
        self.shipped = False

    def get_total(self):
        """ Calculates the total price of melon order. """

        base_price = 5

        total = (1 + self.tax) * self.qty * base_price

        if self.species == 'Christmas melon':
            total *= 1.5
        
        return total


    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""

    def __init__(self, species, qty):
        """Initialize melon order attributes"""
        super(DomesticMelonOrder, self).__init__(species=species, 
                                                 qty=qty,
                                                 order_type='domestic',
                                                 tax=0.08)
        

class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes"""

        super(InternationalMelonOrder, self).__init__(species=species, 
                                                      qty=qty, 
                                                      order_type="international",
                                                      tax=0.17)

        self.country_code = country_code


    def get_total(self):
        """ Get the total of an international order 
        and adds a surcharge for not reaching a minimum number of melons.  

        """

        total = super(InternationalMelonOrder, self).get_total()

        if self.qty < 10:
            total += 3

        return total


    def get_country_code(self):
        """Return the country code."""

        return self.country_code


class GovernmentMelonOrder(AbstractMelonOrder):
    """ Melon orders for the Government. """

    def __init__(self, species, qty):
        """ Initialize melon order for Government. """

        super(GovernmentMelonOrder, self).__init__(species=species,
                                                    qty=qty,
                                                    order_type="government",
                                                    tax=0)

        self.passed_inspection = False 

    def mark_inspection(self, passed):
        """ Update order inspection status. """

        self.passed_inspection = passed