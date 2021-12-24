from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

if __name__ == '__main__':
    menu = Menu()
    coffee_maker_sys = CoffeeMaker()
    money_sys = MoneyMachine()
    while True:
        cmd = input(f'What would you like? ({menu.get_items()[:-1]}) ')
        if cmd == 'off':
            break
        elif cmd == 'report':
            coffee_maker_sys.report()
            money_sys.report()
