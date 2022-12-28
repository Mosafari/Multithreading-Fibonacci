# importing modules
import logging
import threading

# fibunacci func
def fib(n,index):
    global result
    """Calculate the Nth fibonacci number"""
    logging.info("Thread {}: ({}th fibonacci number) -- starting".format(index,n))
    if n < 0:
        raise ValueError('Negative numbers are not supported')
    elif n == 0:
        result= 0
    elif n <= 2:
        result= 1

    result= fib(n - 2) + fib(n - 1)
    logging.info("Thread {}: ({}th fibonacci number) -- finishing".format(index,n))
    


# main 


    # get the number of fibonacci sequence



    # create and start threads



