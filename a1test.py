"""
Test script for module a1

When run as a script, this module invokes several procedures that
test the various functions in the module a1.

Author: SYLVESTER KPEI 
Date:   9/20/2024
"""   
import introcs
import a1
def testA():
    """    
    Test procedure for Part A. This is a test procedure that tests
    how a string with at least one space can be broken up.
    """
    print('Testing part A')
    def test_before_space():
        #numbers and letters with single space
        result= before_space('4.502 Euros')
        introcs.assert_equals('4.502', result)

        #multiple space
        result= before_space('It is 4.502')
        introcs.assert_equals('It', result)

        #space begins
        result= before_space(' 4.502')
        introcs.assert_equals('', result)

        #only letters with single space
        result= before_space('Change it')
        introcs.assert_equals('Change', result)

    def test_after_space():
        #numbers and letters with single space
        result= after_space('4.502 Euros')
        introcs.assert_equals('Euros', result)

        #multiple space
        result= after_space('It is 4.502')
        introcs.assert_equals('is 4.502', result)

        #space ends
        result= after_space('4.502 ')
        introcs.assert_equals('', result)

        #only letters with single space
        result= after_space('Change it')
        introcs.assert_equals('it', result)

    test_before_space()
    test_after_space()



def testB():
    """
    Test procedure for Part B. This is a test procedure that tests how a JSON
    string is processed by extracting the local currency and the converted currency
    from the JSON string
    """
    def test_get_src():
        print('Testing get_src')
        #JSON with 'src'
        result=get_src('{ "src":"2.5 United States Dollars", "dst":"64.375 Cuban Pesos", "valid":true, "err":"" }')
        introcs.assert_equals('2.5 United States Dollars', result)

        #JSON with 'src' removed
        result=get_src('{"dst":"64.375 Cuban Pesos", "valid":true, "err":"" }')
        introcs.assert_equals('',result)

        #JSON with no 'src' value
        result=get_src('{ "src":"", "dst":"64.375 Cuban Pesos", "valid":true, "err":"" }')
        introcs.assert_equals('',result)


    def test_get_dst():
        print('Testing get_dst')
        #Valid JSON with 'dst'
        result=get_dst('{ "src":"2.5 United States Dollars", "dst":"64.375 Cuban Pesos", "valid":true, "err":"" }')
        introcs.assert_equals('64.375 Cuban Pesos', result)

        #JSON with 'dst' removed
        result=get_dst('{ "src":"2.5 United States Dollars", "valid":true, "err":"" }')
        introcs.assert_equals('', result)

        #JSON with no 'dst' value
        result=get_dst('{ "src":"2.5 United States Dollars", "dst":"", "valid":true, "err":"" }')
        introcs.assert_equals('', result)

    def test_has_error():
        print('Testing test_has_error')
        #Valid JSON with no error
        result=has_error('{ "src":"2.5 United States Dollars", "dst":"64.375 Cuban Pesos", "valid":true, "err":"" }')
        introcs.assert_equals(False, result)

        #inValid JSON with error message
        result=has_error('{ "src":"", "dst":"", "valid":false, "err":"Currency amount is invalid." }')
        introcs.assert_equals(True, result)

        #valid JSON with error message
        result=has_error('{ "src":"2.5 United States Dollars", "dst":"64.375 Cuban Pesos", "valid":false, "err":"Currency amount is invalid." }')
        introcs.assert_equals(False, result)


    test_get_src()
    test_get_dst()
    test_has_error()
def testC():
    """
    Test procedure for Part C. This test procedure tests how the response to a
    query is produced in the form of a JSON string.
    """
    def test_currency_response():
        print('Testing part C')
        # valid test
        result= currency_response("USD", "EUR", 50.0)
        introcs.assert_equals('{ "src":"USD-50.0", "dst":"<EUR-amt>", "valid":true, "err":"" }',result)

        #old is invalid
        result=currency_response("US ", "EUR", 50.0)
        introcs.assert_equals('{ "src":"", "dst":"", "valid":false, "err":"Invalid code for src" }',result)

        #new is invalid
        result=currency_response("USD", "EUP", 50.0)
        introcs.assert_equals('{ "src":"", "dst":"", "valid":false, "err":"Invalid code for dst" }',result)

        #amt is invalid
        result=currency_response("USD", "EUR", 50)
        introcs.assert_equals('{ "src":"", "dst":"", "valid":false, "err":"Invalid code for amt" }',result)


def testD():
    """
    Complete Test procedure for Part D
    """
    pass

testA()
testB()
testC()
testD()
print('Module a1 passed all tests.')
