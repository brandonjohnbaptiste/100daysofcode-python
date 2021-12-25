from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

if __name__ == '__main__':
    menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()
    while True:
        cmd = input(f'What would you like? ({menu.get_items()[:-1]}) ')
        if cmd == 'off':
            break
        elif cmd == 'report':
            coffee_maker.report()
            money_machine.report()
        elif cmd == 'latte' or 'espresso' or 'cappuccino':
            drink = menu.find_drink(cmd)
            if coffee_maker.is_resource_sufficient(drink):
                money_machine.make_payment(drink.cost)
                coffee_maker.make_coffee(drink)
