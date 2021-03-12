"""
Library of search algorithms.

Contains a binary search algorithm and a linear search algorithm.

:func: binary_search : binary search
:func: linear_search : linear search
"""

import logging


def binary_search(sought, iterable):
    """
    Returns the result of a binary search of an iterable.
    
    - Start amid a sorted iterable and bound the search at each end.  
    - If the current element exceeds the sought one, raise the lower bound 
    and try again halfway between the bounds.
    - Or, if the sought element exceeds the current one, drop the upper bound 
    and try again halfway between the bounds.
    - Else, return the current element.
    
    :param sought: any type in the iterable
    :param iterable: any iterable object
    
    :return: any type in the iterable
    
    Restrictions: Iterable must be an iterable object of non-zero length
    """
    start = 0
    end = len(iterable)
    i = end//2
    logging.info("Beginning binary_search for %s", sought)
    while (start < end):
        logging.debug("start %s, i %s, iterable[i] %s, end %s", start, i, iterable[i], end)
        if iterable[i] == sought:
            logging.info("binary_search successful, returning %s at index %s", iterable[i], i)
            return iterable[i]
        elif iterable[i] > sought:
            end = i
            i = (start + end)//2
        else:
            start = i
            i = (start + end)//2
    logging.info("binary_search failed!")
        
        
def linear_search(sought, iterable):
    """
    Returns the result of a linear search of an iterable.
    
    Compare each element of the iterable to the sought one and return it if they match.
    
    :param sought: any type in the iterable
    :param iterable: any iterable object
    
    :return: any type in the iterable
    
    Restrictions: Iterable must be an iterable object of non-zero length
    """
    logging.info("Beginning linear_search for %s", sought)
    for i in iterable:
        if i == sought:
            logging.info("linear_search successful, returning %s at index %s", iterable[i], i)
            return i

logging.basicConfig(filename='mynextlog.log', level=logging.INFO, format='%(asctime)s %(message)s')
print(binary_search(30, [i+10 for i in range(100000)]))
