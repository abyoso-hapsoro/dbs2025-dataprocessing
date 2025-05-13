import inspect


def print_success():
    caller = inspect.currentframe().f_back
    print(f"[PASS] {caller.f_code.co_name}")
