def get_methods_list() -> list:
    import inspect
    return inspect.getmembers(coding, inspect.ismodule)