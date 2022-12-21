import typing


def add_ingot(purse: typing.Dict[str, int]) -> typing.Dict:
    purse_copy = purse
    if purse_copy.get("gold_ingots") is not None:
        purse_copy["gold_ingots"] += 1
    else:
        purse_copy["gold_ingots"] = 1
    return purse_copy


def get_ingot(purse: typing.Dict[str, int]) -> typing.Dict:
    purse_copy = purse
    if purse_copy.get("gold_ingots") > 1:
        purse_copy["gold_ingots"] -= 1
    elif purse_copy.get("gold_ingots") is not None:
        del purse_copy["gold_ingots"]
    return purse_copy


def empty(purse: typing.Dict[str, int]) -> typing.Dict:
    purse_copy = {}
    return purse_copy

if __name__ == "__main__":
    purse = {}
    purse_copy = add_ingot(get_ingot(add_ingot(empty(purse))))
    print(purse_copy)
