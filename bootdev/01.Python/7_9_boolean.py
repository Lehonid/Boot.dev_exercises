def does_attack_hit(attack_roll, armor_class):
    if (attack_roll != 1) & (attack_roll >= armor_class) :
        return True
    elif attack_roll == 20 :
        return True
    else :
        return false

does_attack_hit (20, 200)

does_attack_hit (1, 200)


def does_attack_hit(attack_roll, armor_class):
    if ((attack_roll != 1) and (attack_roll >= armor_class)) or (attack_roll == 20) :
        return True
    else :
        return False


### Attention false =! False   pas de "&"" mais "and"
# regarde petit newbie !
def does_attack_hit(attack_roll, armor_class):
    return (attack_roll != 1 and attack_roll >= armor_class) or (attack_roll == 20)
