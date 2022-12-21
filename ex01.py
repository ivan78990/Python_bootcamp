from ex00 import add_ingot, empty


def split_booty(*purses):
    purse_one = (purses[0])
    purse_two = (purses[0])
    purse_three = (purses[0])
    total_ingot = 0
    for purse in purses:
        if purse.get("gold_ingots") is not None:
            total_ingot += purse["gold_ingots"]
    if total_ingot % 3 == 0:
        while total_ingot != 0:
            purse_one = add_ingot(purse_one)
            purse_two = add_ingot(purse_two)
            purse_three = add_ingot(purse_three)
            total_ingot -= 3
    if total_ingot % 3 == 1:
        purse_one = add_ingot(purse_one)
        total_ingot -= 1
    if total_ingot % 3 == 2:
        purse_two = add_ingot(purse_two)
        total_ingot -= 1
    return purse_one, purse_two, purse_three


if __name__ == "__main__":
    purse_one = {"melon": 20}
    purse_two = add_ingot(add_ingot(add_ingot(empty(purse_one))))
    purse_three = add_ingot(add_ingot(empty(purse_one)))
    print(purse_one, purse_two, purse_three)
    print(split_booty(purse_one, purse_two, purse_three))

