import re
import random

def roll(string):
    many_dices = re.split(r'\s\+\s', string)
    print(many_dices)
    dices = list()
    modifier = list()
    for i in many_dices:
        dice = re.match(r'(\d+)d(\d+)', i)
        try:
            dices.append(dice.groups())
        except AttributeError:
            pass
        mod = re.search(r'\d*\w?', i)
        try:
            modifier.append(eval(mod.group()))
        except SyntaxError:
            pass

    result = list()
    for vals in dices:
        _temp = [random.choice(range(1, int(vals[1])+1)) for _ in range(1, int(vals[0])+1)]
        for i in _temp:
            result.append(i)
    if len(modifier) > 0:
        result.append(modifier[0])
    return f'Dices - {result} \nTotal - {sum(result)} '
    print(result)
    print(sum(result))

if __name__ == '__main__':
    roll('1d6')
    roll('1d6 + 1d10')
    roll('1d20')
    roll('1d20 + 2d10 + 3d6 + 5')
    roll('1d100 + 3d6 + 4')
    roll('10d10')
    roll('10d100')