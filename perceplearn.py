import argparse
import json

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument()
    parser.add_argument()
    parser.add_argument()

    args = parser.parse_args()




if __name__ == '__main__':
    main()

parser.add_argument('integers', metavar='N', type=int, nargs='+')
parser.add_argument('--sum', dest='accumulate', action='store_const',const=sum, default=max)
