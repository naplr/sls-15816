from os import listdir
import sys
import numpy as np


def process_lines(lines):
    return [int(l.split()[2]) for l in lines]


if __name__ == '__main__':
    with open ('./time.csv', 'w+') as out:
        for fp in sorted(list(listdir('./time-logs'))):
            with open ('./time-logs/{}'.format(fp), 'r') as f:
                name, cnf, time = fp[:-4].split('-')
                lines = f.readlines()

                idx = 0
                while lines[idx].startswith('#'):
                    idx += 1

                bests = process_lines(lines[idx:idx+10])

                out.write(
                    '{}\t{}\t{}\t{}\t{}\n'.format(name, cnf, time, min(bests), np.mean(bests))
                )
