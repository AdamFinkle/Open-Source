"""
Library of testing parameters.

Classes: None

:func: arr : Returns list of test parameters.
"""

def arr(): 
    """
    Returns a list of test parameters.
    
    Returns a list of tuples, each of which contains a sought number
    and corresponding range wherein to find it.
    
    :return: List of tuples
    """
    return [((30, [i+10 for i in range(100000)]), 30),
           ((-30, [i+10 for i in range(100000)]), -30)]