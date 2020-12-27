#!/usr/bin/python3

# multiplication.py
# A program that teaches multiplication
# Copyright (C) 2020 Scott C. MacCallum
# Email: scm@pdp10.org

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

def facts():
    print('')
    multiplicand = int(input('What facts do you want to see? '))
    for multiplier in range(13):
        product = multiplicand * multiplier
        print(f'{multiplicand} x {multiplier} = {product}')

def table():
    print('')
    print('X ', end='')
    for multiplier in range(1,13):
        print(f'{multiplier} ', end='')

    print('')
    print('2 ', end='')
    multiplicand = 2
    for multiplier in range(1,13):
        product = multiplicand * multiplier
        print(f'{product} ', end='')

    print('')
    multiplicand = 3
    print('3 ', end='')
    for multiplier in range(1,13):
        product = multiplicand * multiplier
        print(f'{product} ', end='')

    print('')
    multiplicand = 4
    print('4 ', end='')
    for multiplier in range(1,13):
        product = multiplicand * multiplier
        print(f'{product} ', end='')

    print('')
    multiplicand = 5
    print('5 ', end='')
    for multiplier in range(1,13):
        product = multiplicand * multiplier
        print(f'{product} ', end='')

    print('')
    multiplicand = 6
    print('6 ', end='')
    for multiplier in range(1,13):
        product = multiplicand * multiplier
        print(f'{product} ', end='')

    print('')
    multiplicand = 7
    print('7 ', end='')
    for multiplier in range(1,13):
        product = multiplicand * multiplier
        print(f'{product} ', end='')

    print('')
    multiplicand = 8
    print('8 ', end='')
    for multiplier in range(1,13):
        product = multiplicand * multiplier
        print(f'{product} ', end='')

    print('')
    multiplicand = 9
    print('9 ', end='')
    for multiplier in range(1,13):
        product = multiplicand * multiplier
        print(f'{product} ', end='')

    print('')
    multiplicand = 10
    print('10 ', end='')
    for multiplier in range(1,13):
        product = multiplicand * multiplier
        print(f'{product} ', end='')

    print('')
    multiplicand = 11
    print('11 ', end='')
    for multiplier in range(1,13):
        product = multiplicand * multiplier
        print(f'{product} ', end='')

    print('')
    multiplicand = 12
    print('12 ', end='')
    for multiplier in range(1,13):
        product = multiplicand * multiplier
        print(f'{product} ', end='')

def main():
    facts()
    table()

if __name__ == "__main__":
    main()
