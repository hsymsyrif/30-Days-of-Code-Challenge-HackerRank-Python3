#!/bin/python3

import sys

if __name__ == '__main__':
    n = int(input().strip())  # Read the size of the array (not actually needed for logic)
    arr = list(map(int, input().rstrip().split()))  # Read the array elements
    print(" ".join(map(str, arr[::-1])))  # Print the reversed array as a space-separated string
