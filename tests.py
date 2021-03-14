"""
Library of tests of library.py

Classes: None

:func: test_binary_search : check if binary_search returns right value
:func: test_linear_search : check if linear_search returns right value

:raises: AssertionError : tested function returned wrong value
:raises: AssertionError : tested function took too long
"""

import pytest 
import library
import test_parameters
import time



# RESULT TESTING

@pytest.mark.parametrize("test_inputs, expected", test_parameters.arr())
def test_binary_search(test_inputs, expected):
    """
    Asserts that binary_search returns right value.
    
    Assert that the result of binary search is the search parameter.
    
    :param test_inputs: any
    :param expected: any
    
    :raises: AssertionError: binary_search returned wrong value
    """
    assert library.binary_search(*test_inputs) == expected

    
@pytest.mark.parametrize("test_inputs, expected", test_parameters.arr())
def test_linear_search(test_inputs, expected):
    """
    Asserts that linear_search returns right value.
    
    Assert that the result of binary search is the search parameter.
    
    :param test_inputs: any
    :param expected: any
    
    :raises: AssertionError: binary_search returned wrong value
    """
    assert library.linear_search(*test_inputs) == expected

    
    
# PERFORMANCE TESTING
    
@pytest.mark.parametrize("test_inputs, expected", test_parameters.arr())
def test_binary_search_performance(test_inputs, expected):
    """
    Asserts that binary_search works fast enough.
    
    Assert that the time of binary_search is tolerable.
    
    :param test_inputs: any
    :param expected: any
    
    :raises: AssertionError: binary_search was too slow
    """
    start = time.time()
    result = library.binary_search(*test_inputs)
    assert abs(time.time() - start) < 0.01

    
@pytest.mark.parametrize("test_inputs, expected", test_parameters.arr())
def test_linear_search_performance(test_inputs, expected):
    """
    Asserts that linear_search works fast enough.
    
    Assert that the time of linear_search is tolerable.
    
    :param test_inputs: any
    :param expected: any
    
    :raises: AssertionError: linear_search was too slow
    """
    start = time.time()
    result = library.linear_search(*test_inputs)
    assert abs(time.time() - start) < 0.01
