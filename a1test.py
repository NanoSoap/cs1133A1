"""
Test script for module a1

When run as a script, this module invokes several procedures that 
test the various functions in the module a1.

Author: Tao Ge(tg367), Xinhui Yu(xy423)
Date:   02/27/2020
"""
import introcs
# introcs.urlread('http://www.cornell.edu')
import a1

def testA():
    """
    Test procedure for Part A
    """
    #space in middle of string
    result=a1.before_space('4.502 Euros')
    introcs.assert_equals('4.502', result)

    #space with more than one space
    result=a1.before_space('4.502   Euros')
    introcs.assert_equals('4.502', result)

    #space at beginning
    result=a1.before_space(' 4.502 Euros')
    introcs.assert_equals('', result)

    #space at beginning and more than one space
    result=a1.before_space('   4.502   Euros')
    introcs.assert_equals('',result)


    #space in middle of string
    result=a1.after_space('4.502 Euros')
    introcs.assert_equals('Euros', result)

    #space with more than one space
    result=a1.after_space('4.502   Euros')
    introcs.assert_equals('  Euros', result)

    #space at beginning
    result=a1.after_space(' 4.502 Euros')
    introcs.assert_equals('4.502 Euros', result)

    #space at beginning and more than one space
    result=a1.after_space('   4.502  Eruos  ')
    introcs.assert_equals('  4.502  Eruos  ',result)


def testB():
    """
    Test procedure for Part B
    """

    #1st test for first_inside_quotes(s)
    result=a1.first_inside_quotes('A "B C" D')
    introcs.assert_equals('B C',result)

    #2nd test for first_inside_quotes(s)
    result=a1.first_inside_quotes('A "B C" D "E F" G')
    introcs.assert_equals('B C',result)

    #test for get_lhs
    result=a1.get_lhs('{"ok":true, "lhs":"2 Namibian Dollars", \
        "rhs":"2 Lesotho Maloti", "err":""}')
    introcs.assert_equals('2 Namibian Dollars', result)

    #test for get_rhs
    result=a1.get_rhs('{"ok":true, "lhs":"2 Namibian Dollars", \
        "rhs":"2 Lesotho Maloti", "err":""}')
    introcs.assert_equals('2 Lesotho Maloti', result)

    #correct call for has_error
    result=a1.has_error('{ "ok":true, "lhs":"2.5 United States Dollars", \
        "rhs":"64.375 Cuban Pesos", "err":"" }')
    introcs.assert_equals(False, result)

    #wrong call for has_error
    result=a1.has_error('{ "ok":false, "lhs":"23 AAA", "rhs":\
        "2.5 United States Dollars", "err":"Source currency code is invalid." }')
    introcs.assert_equals(True, result)


def testC():
    """
    Test procedure for Part C
    """

    #1st test for currency_response
    result=a1.currency_response('USD', 'CNY', 3.0)
    introcs.assert_equals('{ "ok":true, "lhs":"3 United States Dollars", \
"rhs":"20.642538 Chinese Yuan", "err":"" }', result)
    
    #2nd test for currency_response
    result=a1.currency_response('EGP', 'GGP', 2.8)
    introcs.assert_equals('{ "ok":true, "lhs":"2.8 Egyptian Pounds", \
"rhs":"0.13421978485552 Guernsey Pounds", "err":"" }',result)

    #3rd test for currency_response
    result=a1.currency_response('KES','LKR', 10.8)
    introcs.assert_equals('{ "ok":true, "lhs":"10.8 Kenyan Shillings", \
"rhs":"18.40768228849 Sri Lankan Rupees", "err":"" }', result)


def testD():
    """
    Test procedure for Part D
    """
    #correct call for is_currency
    result=a1.is_currency('CNY')
    introcs.assert_equals(True, result)

    #wrong call for is_currency
    result=a1.is_currency('AAA')
    introcs.assert_equals(False, result)

    #test for exchange(src, dst, amt)
    result=a1.exchange('USD', 'CNY', 3.0)
    introcs.assert_floats_equal(20.642538, result)


testA()
testB()
testC()
testD()
print('Module a1 passed all tests.')