from os import listdir
import numpy as np


def process_lines(lines):
    return [int(l.split()[2]) for l in lines]


if __name__ == '__main__':
    with open ('./sweep.csv', 'w+') as out:
        for fp in sorted(list(listdir('./wp-sweep'))):
            with open ('./wp-sweep/{}'.format(fp), 'r') as f:
                num = fp[5:7]
                lines = f.readlines()

                idx = 0
                while lines[idx].startswith('#'):
                    idx += 1

                bests = process_lines(lines[idx:idx+10])

                out.write(
                    '{}\t{}\t{}\n'.format(num, min(bests), np.mean(bests))
                )
