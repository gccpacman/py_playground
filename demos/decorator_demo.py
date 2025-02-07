import time
# from icecream import ic

"""
参考链接:
https://freedium.cfd/https://python.plainenglish.io/5-python-decorators-that-will-transform-your-coding-workflow-38a9c199f7d9

Python decorators provide an elegant way to enhance and extend the functionality of your code. They not only reduce redundancy but also make your codebase more modular and readable.
Python 装饰器提供了一种优雅的方式来增强和扩展代码的功能。它们不仅减少了冗余，还使代码库更加模块化和易于阅读。

As Donald Knuth once remarked, "Programs are meant to be read by humans and only incidentally for computers to execute."
正如唐纳德·克努斯曾经所说：“程序是为了被人类阅读而编写的，仅仅是偶尔让计算机执行。”

Decorators embody this philosophy by enabling cleaner, more maintainable code.
装饰器体现了这一理念，通过使代码更清晰、更易维护。

"""

def time_logger(func):
    # time_logger 是一个简单的装饰器，直接返回 wrapper 函数
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"Function '{func.__name__}' took {end_time - start_time:.4f} seconds.")
        return result
    return wrapper

@time_logger
def process_time_logger(n):
    time.sleep(n)  # Simulate a delay
    return f"Processed {n} seconds of data."

# print(process_time_logger(2))

# ---

def retry(retries=3, delay=1):
    # retry 是一个带参数的装饰器，所以需要多一个 decorator 方法来接收参数
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {attempt + 1} failed: {e}")
                    time.sleep(delay)
            raise Exception(f"Function '{func.__name__}' failed after {retries} retries.")
        return wrapper
    return decorator

@retry(retries=5, delay=2)
def process_retry():
    import random
    if random.random() < 0.8:
        raise ValueError("Transient error!")
    return "Data fetched successfully."


# print(process_retry())


# ---
def type_check(*expected_types):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for arg, expected in zip(args, expected_types):
                if not isinstance(arg, expected):
                    raise TypeError(f"Expected {expected}, got {type(arg)}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@type_check(int, int)
def add(a, b):
    return a + b

# print(add(1, 2))
# print(add(1, "2")) # Raises a TypeError


# ---

def debug(func):
    def wrapper(*args, **kwargs):
        print(f"Calling '{func.__name__}' with args: {args} kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"'{func.__name__}' returned: {result}")
        return result
    return wrapper

@debug
def multiply(a, b):
    return a * b

def multiply_no_decorator(a, b):
    return a * b


# print(multiply(3, "4"))
# print(multiply_no_decorator(3, "4"))


# ---

def rate_limiter(max_calls, period=1):
    """
    rate_limiter 是一个限流装饰器，用于限制函数在指定时间段内的调用次数。
    
    参数:
    max_calls (int): 在指定时间段内允许的最大调用次数。
    period (int): 时间段的长度（以秒为单位）。
    """
    def decorator(func):
        last_calls  = []
        def wrapper(*args, **kwargs):
            nonlocal last_calls
            current_time = time.time()
            # 移除超出时间段的调用记录
            while last_calls and current_time - last_calls [0] > period:
                last_calls .pop(0)
            if len(last_calls ) < max_calls:
                last_calls .append(current_time)
                return func(*args, **kwargs)
            else:
                raise Exception(f"Rate limit exceeded: {max_calls} calls in {period} seconds.")
        return wrapper
    return decorator

@rate_limiter(max_calls=8, period=10)
def process_rate_limiter():
    """
    process_rate_limiter 是一个示例函数，使用 rate_limiter 装饰器来限制调用频率。

    """
    time.sleep(1)  # 模拟处理时间
    return f"Processed data..."

# 示例调用
for i in range(10):
    try:
        print(process_rate_limiter())
    except Exception as e:
        print(e)
        