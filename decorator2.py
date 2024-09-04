import time
from functools import wraps
from typing import Any
from typing import Callable
from typing import Optional

def debug(fn: Callable) -> Callable:
    """Prints the arguments and return value of the decorated function."""
    @wraps(fn)
    def debugger(*args: Any, **kwargs: Any) -> Any:
        print(f"Args: {args}")
        print(f"Kwargs: {kwargs}")
        print(f"Function {fn.__name__}called with args: {args} and kwargs: {kwargs}")
        fn_result = fn(*args, **kwargs)
        print(f"Function {fn.__name__} returned: {fn_result}")
        return fn_result
    return debugger

@debug
def do_something(a: int, b: int, c: Optional[int] = None) -> int:
    return a + b if c is None else a + b + c

@debug
def do_something2(a: int, b: int, c: Optional[int] = None) -> int:
    return a - b if c is None else a - b - c

do_something(1, 2, 3)
do_something2(1, 2, 3)

# The @wraps decorator is used to preserve the metadata of the original function.
# The @wraps decorator is used to preserve the metadata of the original function.
# The @wraps decorator is used to preserve the metadata of the original function.
