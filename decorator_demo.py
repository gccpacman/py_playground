import time
from icecream import ic

def time_logger(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        ic(f"Function '{func.__name__}' took {end_time - start_time:.4f} seconds.")
        return result
    return wrapper




@time_logger
def process_data(n):
    time.sleep(n)  # Simulate a delay
    return f"Processed {n} seconds of data."

ic(process_data(2))