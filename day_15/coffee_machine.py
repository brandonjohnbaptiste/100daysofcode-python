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


if __name__ == '__main__':
    while True:
        command = input('What would you like? (espresso/latte/cappuccino: ')
        if command == 'off':
            break
        elif command == 'report':
            report_resources()
