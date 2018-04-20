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


if __name__ == '__main__':
    assert robot(1) == '1'
    assert robot(2) == '2'
    assert robot(4) == '4'

    assert robot(3) == 'fizz'
    assert robot(6) == 'fizz'
    assert robot(9) == 'fizz'

    assert robot(5) == 'buzz'
    assert robot(10) == 'buzz'
    assert robot(20) == 'buzz'

    assert robot(15) == 'fizzbuzz'
    assert robot(30) == 'fizzbuzz'
    assert robot(45) == 'fizzbuzz'