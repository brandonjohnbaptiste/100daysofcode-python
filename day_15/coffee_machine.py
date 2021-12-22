#!/usr/bin/evn python3

MENU = {
    'espresso': {
        'ingredients': {
            'water': 50,
            'milk': 0,
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
    for ingredient in MENU[drink]['ingredients']:
        if MENU[drink]['ingredients'][ingredient] > resources[ingredient]:
            print(f'Sorry there is not enough {ingredient}')
            return False
    return True


def make_drink(drink):
    for ingredient in resources:
        resources[ingredient] -= MENU[drink]['ingredients'][ingredient]


def collect_coins(drink):
    global money, resources
    print('Please insert coins.')
    quarters = float(input('how many quarters? '))
    dimes = float(input('how many dimes? '))
    nickles = float(input('how many nickles? '))
    pennies = float(input('how many pennies? '))

    coin_total = (quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01)
    cost = MENU[drink]['cost']

    change_due = bool(coin_total - cost > 0.0)
    if change_due:
        print(f'Here is ${coin_total - cost:.2f} in change')

    if coin_total >= cost:
        money += cost
        make_drink(drink)
        print(f'Here is your {drink} ☕️. Enjoy!')
    else:
        print('Sorry that\'s not enough money. Money refunded.')


if __name__ == '__main__':
    while True:
        command = input('What would you like? (espresso/latte/cappuccino): ')
        # TODO: implement a more efficient system for command detection
        if command == 'off':
            break
        elif command == 'report':
            report_resources()
        elif command == 'latte':
            if check_resources('latte'):
                collect_coins('latte')
        elif command == 'espresso':
            if check_resources('espresso'):
                collect_coins('espresso')
        elif command == 'cappuccino':
           if check_resources('cappuccino'):
               collect_coins('cappuccino')
