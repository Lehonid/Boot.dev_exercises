def should_serve_customer2(customer_age, on_break, time):
    return (customer_age >= 21) and (not(on_break)) and ((time > 5 ) and (time <10))


def should_serve_customer1(customer_age, on_break, time):
    if customer_age < 21:
        return False
    if on_break:
        return False
    if time < 5 or time > 10:  # je ne comprends pas bien ...
        return False  # ah ok !
    return True

