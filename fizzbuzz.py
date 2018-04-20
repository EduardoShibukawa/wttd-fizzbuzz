"""
Regras do Fizzbuzz

1. Se a posição for múltipla de 3: fizz
2. Se a posição for múltipla de 5: buzz
3. Se a posição for multipla de 3 e 5: fizzbuzz
4. Para qualquer outra posição fale o próprio nº
"""

from functools import partial


def robot(pos):
    multiple_of = lambda  base, num: num % base == 0
    multiple_of_3 = partial(multiple_of, 3)
    multiple_of_5 = partial(multiple_of, 5)

    if (multiple_of_3(pos)
            and multiple_of_5(pos)):
        return 'fizzbuzz'
    elif multiple_of_3(pos):
        return 'fizz'
    if multiple_of_5(pos):
        return 'buzz'

    return str(pos)


def assert_equals(result, expected):
    from sys import _getframe

    msg = 'Fail: Line {} got {} expecting {}'

    if result != expected:
        current = _getframe()
        caller = current.f_back
        line = caller.f_lineno
        print(msg.format(line, result, expected))


if __name__ == '__main__':
    assert_equals(robot(1), '1')
    assert_equals(robot(2), '2')
    assert_equals(robot(4), '4')

    assert_equals(robot(3), 'fizz')
    assert_equals(robot(6), 'fizz')
    assert_equals(robot(9), 'fizz')

    assert_equals(robot(5), 'buzz')
    assert_equals(robot(10), 'buzz')
    assert_equals(robot(20), 'buzz')

    assert_equals(robot(15), 'fizzbuzz')
    assert_equals(robot(30), 'fizzbuzz')
    assert_equals(robot(45), 'fizzbuzz')
