import argparse
from mpages import *


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--url', help='url', type=str)
    args = parser.parse_args()
    if args.url:
        stock_table(args.url)


if __name__ == '__main__':
    main()
