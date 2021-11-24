import sys
from os import listdir
import numpy as np


def process_lines(lines):
    return [int(l.split()[2]) for l in lines]


IMP_VAR = 612


if __name__ == '__main__':
    fp = sys.argv[1]
    with open (fp, 'r') as f:
        idx = 0
        lines = f.readlines()
        line_idx = []
        for idx, l in enumerate(lines):
            if not l.startswith('#'):
                line_idx.append(idx)

        sol = lines[line_idx[1]].split()[3]
        count = len([x for x in sol[:IMP_VAR] if x == '1'])

        print("{}: there are {} positive assignments among the first {} variables".format(fp, count, IMP_VAR))
