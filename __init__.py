'''
    ema-id-tool Author Kajetan Dowda-Tchorzewski

    Based on:
    EV-ID Validator Version 1.1
    Copyright (C) 2014  smartlab Innovationsgesellschaft mbH, Aachen, Germany

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

import checksum
import checksum.count

my_id = 'DE83DUIEN83ZGQ'
matrixed_id = checksum.count.digits_to_matrices(my_id)
print(matrixed_id)

check_equation = checksum.count.check_equation(matrixed_id)
print(check_equation)

reverse_digit = checksum.count.reverse_digit(check_equation)
print(reverse_digit)

check_digit = checksum.count.check_digit(reverse_digit)
print(check_digit)

