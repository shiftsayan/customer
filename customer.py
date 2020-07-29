#!/usr/bin/env python3
from os import listdir
from os.path import join
from pathlib import Path
from random import sample

import argparse


parser = argparse.ArgumentParser(description='Generate lists of custom words.')
parser.add_argument('packs', metavar='pack', nargs='*',
                   help='names of packs to source custom words from')
parser.add_argument('-a', '--all', dest='all', action='store_const',
                   const=True, default=False,
                   help='list all available packs and exit')
parser.add_argument('-l', '--limit', metavar='n', type=int, default=None,
                   help='return at most n custom words')
parser.add_argument('--allow-dupes', dest='allow_dupes', action='store_const',
                   const=True, default=False,
                   help='allow multiple copies of the same word')


PACKS_PATH = 'packs'


def get_packs():
    '''
    Print a new line separated list of all packs and private packs stored in customer/packs.
    '''
    for f in listdir(join(Path(__file__).parent.absolute(), PACKS_PATH)):
        print(f.split('.')[0])


def get_file(pack):
    '''
    Get the file object for a given (possibly private) pack. May raise FileNotFoundError.
    '''
    try:
        return open(join(Path(__file__).parent.absolute(), PACKS_PATH, f'{pack}.pack'))
    except FileNotFoundError:
        return open(join(Path(__file__).parent.absolute(), PACKS_PATH, f'{pack}-private.pack'))


def get_words(packs, limit, allow_dupes):
    '''
    Print a comma separated list of limit words from packs while allow_dupes.
    '''
    words = []
    for pack in packs:
        try:
            with get_file(pack) as f:
                words.extend(f.read().splitlines())
        except FileNotFoundError:
            raise FileNotFoundError(f'{pack} pack not found') from None
    
    if not allow_dupes:
        words = set(words)

    if limit is not None and limit < len(words):
        words = sample(words, limit)

    print(', '.join(words))

if __name__ == "__main__":
    args = parser.parse_args()
    if args.all:
        get_packs()
    else:
        get_words(args.packs, args.limit, args.allow_dupes)
