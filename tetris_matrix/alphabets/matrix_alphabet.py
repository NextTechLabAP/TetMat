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

import sys
from time import sleep

# from tetris_matrix.alphabets.alphabet_defs import ALPHABET_DICT
from alphabet_defs import ALPHABET_DICT


class Matrix_String(object):

    def __init__(self, message, matrix_width=4, matrix_height=8):
        self.h = matrix_height
        self.w = matrix_width
        self.str_message = str(message).upper()

        self.__full_matrix = ["0" * self.w] * self.h
        self.__process()

    def __repr__(self):
        return str(self.__full_matrix)

    def __add__(self, str2):
        return Matrix_String(self.str_message + str2, self.w, self.h)

    def get_disp_matrix(self):
        return self.__disp

    def __update_disp(self):
        for i in range(self.h):
            self.__disp[i] = self.__full_matrix[i][:self.w]

    def __process(self):
        for char in self.str_message:
            if char not in ALPHABET_DICT.keys():
                raise ValueError("Illegal character in message: {}".format(char))
        for ch in self.str_message:
            for i in range(8):
                self.__full_matrix[i] += ALPHABET_DICT[ch][i] + "0"

        self.__disp = ["" * self.w] * self.h
        self.__update_disp()

    def __lshift(self, n=1):
        copy = self.__full_matrix
        for i in range(self.h):
            copy[i] = self.__full_matrix[i][n:] + "0"
        self.__full_matrix = copy
        self.__update_disp()
        # sleep(1)

    def get_sliding(self):
        n = len(self.str_message)
        n = n
        for i in range(n):
            # print(sum(has_more))
            yield self.get_disp_matrix()
            self.__lshift()

    def print_matrix(self, matrix=None):
        if matrix is None:
            matrix = self.get_sliding()
        block_char = "█"
        block_char = "🛑"
        out = ""
        for frame in matrix:
            for line in frame:
                for ch in line:
                    out += block_char if int(ch) else "  "
                out += "\n"
            print(out)
            print()
            sleep(.1)


my_text = Matrix_String("0123456789", 2, 8)
my_text.print_matrix()

for i in my_text.get_sliding():
    print(i, file=sys.stderr)
