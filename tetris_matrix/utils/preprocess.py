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

import os.path
import string

PY_FILE = os.path.join("../alphabets", "alphabet_defs.py")
CHAR_DEFS = "char_defs.txt"

VALID_CHARACTERS = string.ascii_uppercase + string.digits + " .,?!"

if __name__ == "__main__":
    # TODO: Finish writing the PY_FILE template
    PY_HEADER = ('# MIT License\n'
                 '#\n'
                 '# Copyright (c) 2018 Shubham Rao <cshubhamrao@gmail.com>\n'
                 '#\n'
                 '# Permission is hereby granted, free of charge, to any person obtaining a copy\n'
                 '# of this software and associated documentation files (the "Software"), to deal\n'
                 '# in the Software without restriction, including without limitation the rights\n'
                 '# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell\n'
                 '# copies of the Software, and to permit persons to whom the Software is\n'
                 '# furnished to do so, subject to the following conditions:\n'
                 '#\n'
                 '# The above copyright notice and this permission notice shall be included in all\n'
                 '# copies or substantial portions of the Software.\n'
                 '#\n'
                 '# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\n'
                 '# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\n'
                 '# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\n'
                 '# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\n'
                 '# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\n'
                 '# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE\n'
                 '# SOFTWARE.\n'
                 "\n"
                 "# GENERATED USING THE `preprocess.py` script\n"
                 "# DO NOT MODIFY MANUALLY\n"
                 '\n'
                 f'VALID_CHARACTERS = "{VALID_CHARACTERS}"\n'
                 'ALPHABET_DICT = {}\n'
                 '\n')

    CODE_FORMAT = "ALPHABET_DICT['{alphabet}'] = {tup}\n"

    py_file = open(PY_FILE, "w+")
    def_file = open(CHAR_DEFS)

    lines = [line.rstrip(("\n")) for line in def_file]

    py_file.write(PY_HEADER)
    buf = ()
    line_idx = char_idx = 0
    while line_idx < len(lines):
        buf += tuple(c for c in lines[line_idx + 1:line_idx + 9])
        py_file.write(CODE_FORMAT.format(alphabet=VALID_CHARACTERS[char_idx], tup=buf))
        buf = ()
        line_idx += 9
        char_idx += 1

    py_file.close()
    def_file.close()
