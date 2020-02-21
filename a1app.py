"""
User interface for module currency

When run as a script, this module prompts the user for two currencies and 
an amount. It prints out the result of converting the first currency to 
the second.

Author: Tao Ge(tg367), Xinhui Yu(xy423)
Date:   02/21/2020
"""
import a1

l = input('Enter source currency:')
r = input('Enter target currency:')
a = input('Enter original amount:')
if (not(a1.is_currency(l) and a1.is_currency(r))):
    print('Wrong input!')
else:
    res = a1.exchange(l, r, a)
    print('You can exchange '+a+' '+l+' for '+str(res)+' '+r + '.')
