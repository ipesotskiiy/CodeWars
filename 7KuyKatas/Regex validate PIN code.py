def validate_pin(pin):
    return (len(pin)==4 or len(pin) == 6) and pin.isdigit()