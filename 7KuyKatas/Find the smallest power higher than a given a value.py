def find_next_power(val, pow_):
    original_number = int(pow(val, 1/pow_))
    next_power_value = (original_number + 1) ** pow_
    return next_power_value