#!/usr/bin/evn python3

MENU = {
    'espresso': {
        'ingredients': {
            'water': 50,
            'coffee': 18,
        },
        'cost': 1.5,
    },
    'latte': {
        'ingredients': {
            'water': 200,
            'milk': 150,
            'coffee': 24,
        },
        'cost': 2.5,
    },
    'cappuccino': {
        'ingredients': {
            'water': 250,
            'milk': 100,
            'coffee': 24,
        },
        'cost': 3.0,
    }
}

resources = {
    'water': 300,
    'milk': 200,
    'coffee': 100,
}

money = 0.0


def report_resources():
    for value in resources:
        context_marker = 'ml' if value == 'water' or value == 'mil' else 'g'
        print(f'{value.capitalize()}: {resources.get(value)}{context_marker}')
    print(f'Money: ${money}')


def check_resources(drink):
    water_required = MENU[drink]['ingredients']['water']
    milk_required = MENU[drink]['ingredients']['milk']
    coffee_required = MENU[drink]['ingredients']['coffee']

    return bool(water_required <= resources['water']
                and milk_required <= resources['milk']
                and coffee_required <= resources['coffee'])


if __name__ == '__main__':
    while True:
        command = input('What would you like? (espresso/latte/cappuccino: ')
        if command == 'off':
            break
        elif command == 'report':
            report_resources()
        elif command == 'latte':
            check_resources('latte')
        elif command == 'espresso':
            check_resources('espresso')
        elif command == 'cappuccino':
            check_resources('cappuccino')
