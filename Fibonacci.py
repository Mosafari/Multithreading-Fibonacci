# importing modules
import logging
import threading

# fibunacci func
def fib(n):
    print(n)
    global result
    """Calculate the Nth fibonacci number"""
    logging.info("Thread ({}th fibonacci number) -- starting".format(n))
    if n < 0:
        raise ValueError('Negative numbers are not supported')
    elif n == 0:
        result["{}th".format(n)] = 0
    elif n <= 2:
        result["{}th".format(n)] = 1
    else:
        a=0
        b=1
        for i in range(1, n):
            c = a + b
            a = b
            b = c
        result["{}th".format(n)] = b
    logging.info("Thread ({}th fibonacci number) -- finishing".format(n))
    


# main 
if __name__ == '__main__':
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    result = {}
    # get the number of fibonacci sequence
    nums =[]
    for i in range(3):
        num = int(input("Enter a number : "))
        nums.append(num)
    
    print(nums)
    # create and start threads    
    threads = []
    for i,n in enumerate(nums):
        print(n,i)
        logging.info("Main    : create and start thread {}.".format(i+1))
        x = threading.Thread(target=fib, args=(n,))
        threads.append(x)
        x.name = "{}th".format(n)
        x.start()
        
    for index, thread in enumerate(threads):
        logging.info("Main    : before joining thread {}.".format(i+1))
        thread.join()
        print("Result of {} : {}".format(thread.name ,result[thread.name]))
        logging.info("Main    : thread {} done".format(index+1))



