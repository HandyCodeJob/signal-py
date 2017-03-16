#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''signal-py

Usage:
  signal-py ship new <name>...
  signal-py ship <name> move <x> <y> [--speed=<kn>]
  signal-py ship shoot <x> <y>
  signal-py mine (set|remove) <x> <y> [--moored|--drifting]
  signal-py -h | --help
  signal-py --version

Options:
  -h --help     Show this screen.
  --version     Show version.
  --speed=<kn>  Speed in knots [default: 10].
  --moored      Moored (anchored) mine.
  --drifting    Drifting mine.
'''

from __future__ import unicode_literals, print_function
from docopt import docopt

__version__ = "0.1.0"
__author__ = "Sydney Henry"
__license__ = "MIT"


def main():
    '''Main entry point for the signal-py CLI.'''
    args = docopt(__doc__, version=__version__)
    print(args)

if __name__ == '__main__':
    main()