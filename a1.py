
"""
Module for currency exchange

This module provides several string parsing functions to implement a
simple currency exchange routine using an online currency service.
The primary function in this module is exchange.

Author: SYLVESTER sek266
Date:   9/20/2024
"""
import introcs
def exchange(old, new, amt):
    """
    Returns the amount of currency received in the given exchange.

    In this exchange, the user is changing amt money in currency old
    to the currency new. The value returned represents the amount in
    currency new.

    The value returned has type float.

    Parameter old: the currency on hand (the SRC)
    Precondition: old is a string for a valid currency code

    Parameter new: the currency to convert to (the DST)
    Precondition: new is a string for a valid currency code

    Parameter amt: amount of currency to convert
    Precondition: amt is a float
    """

   
def before_space(s):
    """
    Returns a copy of s up to, but not including, the first space
    Parameter s: the string to slice
    Precondition: s is a string with at least one space
    """
    return s[:s.index(' ')]

def after_space(s):
    """
    Returns a copy of s after the first space
    Parameter s: the string to slice
    Precondition: s is a string with at least one space
    """
    return s[s.index(' ')+1:]


def get_src(json):
    start=json.index('"src":"')+len('"src":"')
    end=json.index('"', start)
    result=json[start:end]
    return result

def get_dst(json):
    start=json.index('"dst":"')+len('"dst":"')
    end=json.index('"', start)
    result=json[start:end]
    return result

def has_error(json):
    start= json.index('"valid":')+len('"valid":')
    result= json[start:].strip()[:5]
    return result=='false'

def currency_response(old, new, amount):
    """
    Returns a JSON string that is a response to a currency query.

    A currency query converts amt money in currency old to the
    currency new. The response should be a string of the form

    '{ "src":"<old-amt>", "dst":"<new-amt>", "valid":true, "err":"" }'

    where the values old-amount and new-amount contain the value
    and name for the original and new currencies. If the query is
    invalid, both old-amount and new-amount will be empty, while
    "valid" will be followed by the value false (and "err" will have
    an error message).

    Parameter old: the currency on hand (the SRC)
    Precondition: old is a string with no spaces or non-letters

    Parameter new: the currency to convert to (the DST)
    Precondition: new is a string with no spaces or non-letters

    Parameter amt: amount of currency to convert
    Precondition: amt is a float
    """
    json= introcs.urlread('http://cs1110.cs.cornell.edu/2024fa/a1?from='+old+'&to='+new+'&amt='+str(amount))
    return json
