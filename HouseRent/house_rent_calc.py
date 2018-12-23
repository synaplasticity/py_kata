import math


def rent_for_years(init_rent, perc_increase, increase_interval=1, years=1):
    if years == 1:
        return init_rent

    no_of_increases = math.ceil(years / increase_interval)
    print("inc : ", no_of_increases)

    old_rent = init_rent
    for int in range(1, years, increase_interval):
        new_rent = old_rent + old_rent * (perc_increase / 100)
        print("Old/New : ", int, old_rent)
        old_rent = new_rent

    return new_rent