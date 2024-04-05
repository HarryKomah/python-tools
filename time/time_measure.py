import time
"""
Basic skeleton:

def measure_time(func, *args):
    start_time = time.time()
    if args:
        func(*args)
    else:
        func()
    end_time = time.process_time()
    time_elapsed = end_time - start_time
    return time_elapsed

"""

def stopwatch_decorator(f):
    def wrapper(*args, **kwargs):
        measure_time(f, *args, **kwargs)
    return wrapper

def measure_time(func, *args, cpu=False):
    """
    Measure the execution time of a function.

    Args:
        func (function): The function to be executed and timed.
        *args: Variable length argument list to be passed to the function.
        cpu (bool, optional): If True, measure CPU time instead of wall-clock time. Defaults to False.

    Returns:
        None
"""
    start_time = time.process_time() if cpu else time.time()
    if args:
        func(*args) # star operator will unpack the arguments.
    else:
        func()
    end_time = time.process_time() if cpu else time.time()
    elapsed = end_time - start_time
    seconds = str(elapsed) + " CPU cycle." if cpu else " seconds."
    print(func.__name__ + " executed and finished in " + str(elapsed) + seconds)

# EXAMPLE usage:


@stopwatch_decorator
def hello_world():
    print("Hello World")
    return b"Hello World"

#measure_time(hello_world, cpu=True)

hello_world()
