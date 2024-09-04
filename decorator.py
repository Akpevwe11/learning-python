def decorator(fn: callable) -> callable:
    print("Start decorator function from: ", fn.__name__)
    def wrapper(*args, **kwargs):
        print("Start wrapper function from: ", fn.__name__)
        result = fn(*args, **kwargs)
        print("End wrapper function from: ", fn.__name__)
        return result
    print("End decorator function from: ", fn.__name__)
    return wrapper


#@decorator
def my_function():
    print("Hello from my_function")

#my_function()

decorator_print_hello = decorator(my_function)
decorator_print_hello()
