"""
User interface for module currency

When run as a script, this module prompts the user for two currencies and 
an amount. It prints out the result of converting the first currency to 
the second.

Author: Tao Ge(tg367), Xinhui Yu(xy423)
Date:   02/21/2020
"""
import a1
def exchange(src, dst, amt):
    """
    Returns the amount of currency received in the given exchange.

    In this exchange, the user is changing amt money in currency src 
    to the currency dst. The value returned represents the amount in 
    currency dst.

    The value returned has type float.

    Parameter src: the currency on hand (the LHS)
    Precondition: src is a string for a valid currency code
    
    Parameter dst: the currency to convert to (the RHS)
    Precondition: dst is a string for a valid currency code
    
    Parameter amt: amount of currency to convert
    Precondition: amt is a float
    """
