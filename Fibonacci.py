# importing modules
import logging
import threading

# fibunacci func
def fib(n):
    """Calculate the Nth fibonacci number"""
    if n < 0:
        raise ValueError('Negative numbers are not supported')
    elif n == 0:
        return 0
    elif n <= 2:
        return 1

    return fib(n - 2) + fib(n - 1)
    


# main 


    # get the number of fibonacci sequence



    # create and start threads



