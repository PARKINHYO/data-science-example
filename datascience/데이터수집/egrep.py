import sys, re

if __name__ == '__main__':

    regex = sys.argv[1]

    for line in sys.stdin:

        if re.search(regex, line):
            sys.stdout.write(line)