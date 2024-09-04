from functools import wraps

def timing_decorator(fn: callable) -> callable:
    """Prints the time it takes for a function to execute."""
    @wraps(fn)
    def wrapper(*args, **kwargs):
        import time
        start = time.time()
        result = fn(*args, **kwargs)
        end = time.time()
        print(f"Function {fn.__name__} took: {end - start} seconds")
        return result
    return wrapper

@timing_decorator
def my_function():
    print("Hello from my_function")

my_function()

# The @wraps decorator is used to preserve the metadata of the original function.