import math


def rent_per_month(init_rent, perc_increase, increase_interval=1, years=1):

    no_of_increases = math.ceil(years / increase_interval)
    print("inc : ", no_of_increases)
    if no_of_increases == 1:
        return init_rent

    old_rent = new_rent = init_rent
    for int in range(1, years, increase_interval):
        new_rent = old_rent + old_rent * (perc_increase / 100)
        old_rent = new_rent

    return round(new_rent, 2)


def annual_rent_for_period(init_rent, perc_increase, increase_interval=1,
                           years=1):
    return round(rent_per_month(init_rent, perc_increase, increase_interval,
                 years) * 12
                 * years,
                 2)