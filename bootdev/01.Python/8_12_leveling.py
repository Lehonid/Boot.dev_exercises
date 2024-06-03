def calculate_experience_points(level):
    xp = 0
    for level in range (level, 0, -1):
          xp += ((level - 1)*5)
    return xp

"""
Solution
def calculate_experience_points(level):
    xp = 0
    for i in range(1, level):
        xp += i * 5

    return xp
"""