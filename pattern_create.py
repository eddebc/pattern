#!/usr/bin/env python3
"""
Re-write of Metasploit's pattern_create tool that
creates a unique pattern according to given length
with an omittable argument defining the char map used.
The default map is ascii_uppercase, ascii_lowercase, digits.

Example:
#./pattern_create.py -l 50 -s ABC,def,123
Ad1Ad2Ad3Ae1Ae2Ae3Af1Af2Af3Bd1Bd2Bd3Be1Be2Be3Bf1Bf
"""

from string import digits, ascii_uppercase, ascii_lowercase
from argparse import ArgumentParser, RawDescriptionHelpFormatter
from itertools import accumulate, chain


class RelatedRotor(object):
    """
    Defines the relation between two glyphs ('digits').
    When this glyph completes a cycle, it rotates its bigger brother.
    """
    def __init__(self, next_rotary=None, glyphs=digits):
        self.glyphs = glyphs
        self.rotary = iter(glyphs)
        self.value = next(self.rotary)
        self.next_rotary = next_rotary

    def rotate(self):
        """
        Increment self and brother, if full revolution.
        """
        try:
            self.value = next(self.rotary)
        except StopIteration:
            self.rotary = iter(self.glyphs)
            self.value = next(self.rotary)
            try:
                return self.next_rotary.rotate()
            except AttributeError:
                pass

    def __str__(self):
        return self.value


class RotaryNumber(object):
    """
    A custom number made up of numerous glyphs. Reminds one of the Cryptex.
    Each glyph can rotate to the next possible value. When it completes one
    cycle, it rotates the next glyph.
    """
    def __init__(self, *glyph_lists):
        glyphs = accumulate(chain((None, ), glyph_lists), RelatedRotor)
        next(glyphs)
        self.glyphs = list(glyphs)

    def __iadd__(self, other):
        """rot += 1"""
        for _ in range(other):
            self.glyphs[-1].rotate()
        return self


def cycle_chars(custom_num):
    while True:
        for glyph in custom_num.glyphs:
            yield glyph
        custom_num += 1


def Aa0Number():
    return RotaryNumber(ascii_uppercase, ascii_lowercase, digits)


def pattern_create(length, number=Aa0Number()):
    _cycle = cycle_chars(number)
    for _ in range(length):
        yield next(_cycle)


def parse_args():
    parser = ArgumentParser(description=f"Tool to create a unique pattern. Example:\n#{__file__} -l 50 -s ABC,def,123\nAd1Ad2Ad3Ae1Ae2Ae3Af1Af2Af3Bd1Bd2Bd3Be1Be2Be3Bf1Bf",
                            formatter_class=RawDescriptionHelpFormatter)
    parser.add_argument('-l', '--length', type=int, required=True,
                        help="Length of the pattern")
    parser.add_argument('-s', '--sets', required=False,
                        help="Custom pattern sets such as <ABC,def,123>")
    _args = parser.parse_args()
    if _args.sets:
        _args.sets = _args.sets.split(',')
    return _args


if __name__ == '__main__':
    args = parse_args()
    if args.sets:
        generator = pattern_create(args.length, RotaryNumber(*args.sets))
    else:
        generator = pattern_create(args.length)

    for c in generator:
        print(c, end='')
    print()
