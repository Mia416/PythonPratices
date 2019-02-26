'''
Created on Mar 13, 2017

@author: chenz
'''

import argparse

def get_args():
    parser = argparse.ArgumentParser(description='help')
    parser.add_argument('-s', '--str', type=str, help='quert string', required=True)
    args = parser.parse_args()
    qq = args.str
    return qq


rr = get_args()
print rr
