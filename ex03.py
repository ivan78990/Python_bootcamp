import typing
from ex00 import add_ingot, get_ingot, empty


def my_decorator(func: object) -> typing.Dict:
    """

    :rtype: object
    """
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
    return wrapper


if __name__ == "__main__":
    purse = {}
    purse_copy = add_ingot(get_ingot(add_ingot(empty(purse))))
    @my_decorator
    purse_copy = add_ingot(get_ingot(add_ingot(empty(purse))))

    print(purse_copy)
