# MIT License
#
# Copyright (c) 2018 Shubham Rao <cshubhamrao@gmail.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# GENERATED USING THE preprocess.py script
# DO NOT MODIFY MANUALLY

import string

VALID_CHARACTERS = string.ascii_uppercase + string.digits + " .,?!"
ALPHABET_DICT = {}

ALPHABET_DICT['A'] = ('11111', '10001', '10001', '10001', '11111', '10001', '10001', '10001')
ALPHABET_DICT['B'] = ('11110', '10010', '10010', '11111', '10001', '10001', '10001', '11111')
ALPHABET_DICT['C'] = ('11111', '10001', '10000', '10000', '10000', '10000', '10001', '11111')
ALPHABET_DICT['D'] = ('11100', '10010', '10001', '10001', '10001', '10001', '10010', '11100')
ALPHABET_DICT['E'] = ('11111', '10000', '10000', '11100', '10000', '10000', '10000', '11111')
ALPHABET_DICT['F'] = ('11111', '10000', '10000', '11100', '10000', '10000', '10000', '10000')
ALPHABET_DICT['G'] = ('11111', '10000', '10000', '10000', '10111', '10101', '10001', '11111')
ALPHABET_DICT['H'] = ('10001', '10001', '10001', '11111', '11111', '10001', '10001', '10001')
ALPHABET_DICT['I'] = ('11111', '00100', '00100', '00100', '00100', '00100', '00100', '11111')
ALPHABET_DICT['J'] = ('11111', '00100', '00100', '00100', '00100', '00100', '10100', '11100')
ALPHABET_DICT['K'] = ('10001', '10010', '10100', '11000', '11000', '10100', '10010', '10001')
ALPHABET_DICT['L'] = ('10000', '10000', '10000', '10000', '10000', '10000', '10001', '11111')
ALPHABET_DICT['M'] = ('11011', '10101', '10101', '10101', '10001', '10001', '10001', '10001')
ALPHABET_DICT['N'] = ('10001', '11001', '11001', '10101', '10101', '10011', '10011', '10001')
ALPHABET_DICT['O'] = ('01110', '10001', '10001', '10001', '10001', '10001', '10001', '01110')
ALPHABET_DICT['P'] = ('11111', '10001', '10001', '10001', '11111', '10000', '10000', '10000')
ALPHABET_DICT['Q'] = ('01110', '10001', '10001', '10001', '10001', '10001', '01110', '00001')
ALPHABET_DICT['R'] = ('11111', '10001', '10001', '11111', '11000', '10100', '10010', '10001')
ALPHABET_DICT['S'] = ('11111', '10001', '10000', '10000', '11111', '00001', '10001', '11111')
ALPHABET_DICT['T'] = ('11111', '00100', '00100', '00100', '00100', '00100', '00100', '00100')
ALPHABET_DICT['U'] = ('10001', '10001', '10001', '10001', '10001', '10001', '10001', '11111')
ALPHABET_DICT['V'] = ('10001', '10001', '10001', '10001', '10001', '10001', '01010', '00100')
ALPHABET_DICT['W'] = ('10001', '10001', '10001', '10001', '10101', '10101', '10101', '01010')
ALPHABET_DICT['X'] = ('10001', '11011', '01010', '00100', '00100', '01010', '11011', '10001')
ALPHABET_DICT['Y'] = ('10001', '10001', '10001', '11111', '00100', '00100', '00100', '00100')
ALPHABET_DICT['Z'] = ('11111', '00001', '00010', '00100', '00100', '01000', '10000', '11111')
ALPHABET_DICT['0'] = ('01110', '10001', '10001', '10101', '10101', '10001', '10001', '01110')
ALPHABET_DICT['1'] = ('00100', '01100', '10100', '00100', '00100', '00100', '00100', '11111')
ALPHABET_DICT['2'] = ('11111', '00001', '00001', '00001', '11111', '10000', '10000', '11111')
ALPHABET_DICT['3'] = ('11111', '00001', '00001', '00111', '00001', '00001', '00001', '11111')
ALPHABET_DICT['4'] = ('00010', '00110', '01010', '10010', '10010', '11111', '00010', '00010')
ALPHABET_DICT['5'] = ('11111', '10000', '10000', '10000', '11111', '00001', '00001', '11111')
ALPHABET_DICT['6'] = ('11111', '10001', '10000', '10000', '11111', '10001', '10001', '11111')
ALPHABET_DICT['7'] = ('11111', '00001', '00010', '00010', '00100', '00100', '01000', '01000')
ALPHABET_DICT['8'] = ('11111', '10001', '10001', '11111', '11111', '10001', '10001', '11111')
ALPHABET_DICT['9'] = ('11111', '10001', '10001', '11111', '00001', '00001', '10001', '11111')
ALPHABET_DICT[' '] = ('00000', '00000', '00000', '00000', '00000', '00000', '00000', '00000')
ALPHABET_DICT['.'] = ('00000', '00000', '00000', '00000', '00000', '00000', '00000', '10000')
ALPHABET_DICT[','] = ('00000', '00000', '00000', '00000', '11000', '11000', '01000', '11000')
ALPHABET_DICT['?'] = ('11110', '10010', '00010', '01110', '01000', '01000', '00000', '01000')
ALPHABET_DICT['!'] = ('01000', '01000', '01000', '01000', '01000', '01000', '00000', '01000')