from os import listdir
import sys
import numpy as np


def process_lines(lines):
    return [int(l.split()[2]) for l in lines]


if __name__ == '__main__':
    folder_path = sys.argv[1]
    with open ('./agg-{}.csv'.format(folder_path, 'w+') as out:
        for fp in listdir(folder_path):
            with open ('{}/{}'.format(folder_path, fp), 'r') as f:
                num = fp[-6:-4]
                lines = f.readlines()

                idx = 0
                while lines[idx].startswith('#'):
                    idx += 1

                bests = process_lines(lines[idx:idx+10])

                out.write(
                    '{}\t{}\t{}\t{}\n'.format(num, fp[:-6], min(bests), np.mean(bests))
                )
