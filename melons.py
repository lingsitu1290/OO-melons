"""This file should have our order classes in it."""

class AbstractMelonOrder(object):
    """ Parent class for various types of melon orders. """

    def __init__(self, species, qty):
        """ Initialize all melon order types. """

        self.species = species
        self.qty = qty 
        self.tax = 0.08

    def get_total(self):
        """ Calculates the total price of melon order. """

        base_price = 5
        total = (1 + self.tax) * self.qty * base_price
        return total

    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""

    def __init__(self, species, qty):
        """Initialize melon order attributes"""

        self.shipped = False
        self.order_type = "domestic"
        self.tax = 0.08

        super(DomesticMelonOrder, self).__init__(species, qty)


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes"""

        self.country_code = country_code
        self.shipped = False
        self.order_type = "international"
        self.tax = 0.17

        super(InternationalMelonOrder, self).__init__(species, qty)

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

