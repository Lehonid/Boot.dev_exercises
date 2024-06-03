# 4
def print_status(player_health):
    if player_health == 0 :
        print ("dead")
    print ("status check complete")

# 5
def check_swords_for_army(number_of_swords, number_of_soldiers):
    if number_of_soldiers == number_of_swords :
        answer="correct amount"
    else :
        answer="incorrect amount"
    return answer

# solution des anciens qui savent
def check_swords_for_army(number_of_swords, number_of_soldiers):
    if number_of_soldiers == number_of_swords:
        return "correct amount"
    return "incorrect amount"
