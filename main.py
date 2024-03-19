def calculate_health(current_health, damage_received, armor):
    calculatedValue = damage_received * armor
    currentHealth = current_health - calculatedValue

    print(currentHealth)
    return currentHealth


def average_of_five(a, b, c, d, e):
    calculatedValue = (a + b + c + d + e) / 5

    print(calculatedValue)
    return calculatedValue


calculate_health(100, 10, 0.5)
average_of_five(10, 20, 30, 40, 50)
