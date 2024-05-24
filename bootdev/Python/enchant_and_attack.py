def enchant_and_attack(target_health, damage, weapon):
    enchanted_damage = damage + 10
    new_health = target_health - enchanted_damage
    enchanted_weapon = f"enchanted {weapon}"
    # plus simple    enchanted_weapon = "enchanted " + weapon
    return enchanted_weapon, new_health

