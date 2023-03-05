import random

coffees = [
    'Ethiopia',
    'Kenya',
    'Burundi',
    'El Salvador',
    'Guatemala',
    'Colombia',
    'Indonesia',
    'Costa Rica'
]

methods = [
    'espresso',
    'cappuccino',
    'macchiato',
    'chemex drip coffee',
    'drip coffee',
    'siphon coffee',
    'cold brew',
    'nitro'
]

random_coffee = random.choice(coffees)
random_method = random.choice(methods)

print(f"How about having some {random_coffee} as {random_method}?")
