from typing import Callable


def replace(replace_func: Callable, replace: bool = True):

    def handle_func(func: Callable):
        def handle_args(*args, **kwargs):
            if replace:
                res = replace_func(*args, **kwargs)
            else:
                res = func(*args, **kwargs)
            return res
        return handle_args
    return handle_func


def retry(count: int = 3, stop_retry_func: Callable[[Exception], bool] = None):

    def handle_func(func: Callable):
        def handle_args(*args, **kwargs):
            try:
                res = func(*args, **kwargs)
                return res
            except Exception as e:
                for i in range(count):
                    try:
                        res = func(*args, **kwargs)
                        return res
                    except Exception as e1:
                        if stop_retry_func:
                            flag = stop_retry_func(e)
                            if flag:
                                return None
                return None
        return handle_args
    return handle_func
