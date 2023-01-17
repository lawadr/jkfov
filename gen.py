"""Generate IPS file to patch field of view (FoV) in Jedi Knight: Dark Forces II
or Jedi Knight: Mysteries of the Sith.
"""

import sys
import os
import math
import struct
import argparse


def calc_jk_subs(fov):
    """Return byte substitutions for jk.ips for a given field of view."""
    fov_indices = [10, 16, 22, 28, 34, 40]
    return [(i, fov * 2) for i in fov_indices]


def calc_jkm_subs(fov):
    """Return byte substitutions for jkm.ips for a given field of view."""
    fov_indices = [10, 16, 22, 28, 34, 40, 77]
    subs = [(i, fov * 2) for i in fov_indices]

    float_bytes = struct.pack('<f', math.tan(math.radians(fov / 2)) / 2)
    subs += [(91, float_bytes[2] if float_bytes[1] < 128 else float_bytes[2] + 1)]
    subs += [(92, float_bytes[3])]

    return subs


def main(exe, fov, output):
    """Output patch file for a given executable and field of view."""
    with open(os.path.join(sys.path[0], f'{exe}-fov120.ips'), 'rb') as file:
        data = bytearray(file.read())

    for sub in globals()[f'calc_{exe}_subs'](fov):
        data[sub[0]] = sub[1]

    output.write(data)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__, add_help=False)
    parser.add_argument('exe', choices=['jk', 'jkm'], help='game executable')
    parser.add_argument('fov', type=int, help='field of view in degrees')
    parser.add_argument('-o', "--output", dest='file',
                        type=argparse.FileType('wb'), default='-', help='output to FILE')
    parser.add_argument("-h", "--help", action="help", help="show this help message and exit")

    args = parser.parse_args()
    main(args.exe, args.fov, args.file)
