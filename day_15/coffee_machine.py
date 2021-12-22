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
        context_marker = 'ml' if value == 'water' or value == 'milk' else 'g'
        print(f'{value.capitalize()}: {resources.get(value)}{context_marker}')
    print(f'Money: ${money}')


def check_resources(drink):
    # TODO: return messages if a resource is less than required
    water_required = MENU[drink]['ingredients']['water']
    milk_required = MENU[drink]['ingredients']['milk']
    coffee_required = MENU[drink]['ingredients']['coffee']

    return bool(water_required <= resources['water']
                and milk_required <= resources['milk']
                and coffee_required <= resources['coffee'])


def collect_coins(drink):
    print('Please insert coins.')
    quarters = float(input('how many quarters? '))
    dimes = float(input('how many dimes? '))
    nickles = float(input('how many nickles? '))
    pennies = float(input('how many pennies? '))

    total_money = (quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01)
    cost = MENU[drink]['cost']

    change_due = bool(total_money - cost > 0.0)
    if change_due:
        print(f'Here is ${total_money - cost:.2f} in change')

    if total_money >= cost:
        print(f'Here is your {drink} ☕️. Enjoy!')
    else:
        print('Sorry that\'s not enough money. Money refunded.')


if __name__ == '__main__':
    while True:
        command = input('What would you like? (espresso/latte/cappuccino): ')
        if command == 'off':
            break
        elif command == 'report':
            report_resources()
        elif command == 'latte':
            if check_resources('latte'):
                collect_coins('latte')
        elif command == 'espresso':
            check_resources('espresso')
        elif command == 'cappuccino':
            check_resources('cappuccino')
