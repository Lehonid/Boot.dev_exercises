def check_swords_for_army(number_of_swords, number_of_soldiers):
    if number_of_soldiers == number_of_swords:
        return "correct amount"
    return "incorrect amount"

test = check_swords_for_army (3, 100)

print(test)


def player_status(health):
    if health <= 0 :
        return "dead"
    elif health <=5 :
        return "injured"
    return "healthy"

 # équivaut à 

def player_status(health):
    if health <= 0:
        return "dead"
    elif health <= 5:
        return "injured"
    else:
        return "healthy"