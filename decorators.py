from functools import wraps
import time

# decorator function to measure time taken of fct.
def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        # first item in the args, ie `args[0]` is `self`
        print(f'{func.__name__} Function took {total_time:.4f}s')
        return result
    return timeit_wrapper