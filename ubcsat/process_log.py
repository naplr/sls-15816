from os import listdir
import numpy as np


def process_lines(lines):
    return [int(l.split()[2]) for l in lines]


if __name__ == '__main__':
    with open ('./agg.csv', 'w+') as out:
        for fp in listdir('./logs7'):
            with open ('./logs7/{}'.format(fp), 'r') as f:
                num = fp[-6:-4]
                lines = f.readlines()

                idx = 0
                while lines[idx].startswith('#'):
                    idx += 1

                bests = process_lines(lines[idx:idx+10])

                out.write(
                    '{}\t{}\t{}\t{}\n'.format(num, fp[:-6], min(bests), np.mean(bests))
                )
