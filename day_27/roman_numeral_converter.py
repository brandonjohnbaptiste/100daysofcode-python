def roman_to_int(s):
    nums = {'I': 1, 'V': 5, 'X': 10,
            'L': 50, 'C': 100, 'D': 500,
            'M': 1000}
    symbols = [char for char in s]
    subtract = ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']
    result = 0

    i = 0
    while i < len(symbols):
        symbol = symbols[i]
        if symbols.index(symbol) == len(symbols) - 1:
            result += nums.get(symbol)
            break

        if symbol + symbols[symbols.index(symbol) + 1] in subtract:
            result += nums.get(symbols[symbols.index(symbol) + 1]) - nums.get(symbol)
            print(nums.get(symbols[symbols.index(symbol) + 1]) - nums.get(symbol))
            i += 1
        else:
            result += nums.get(symbol)
            print(nums.get(symbol))

        i += 1

    print(result)
