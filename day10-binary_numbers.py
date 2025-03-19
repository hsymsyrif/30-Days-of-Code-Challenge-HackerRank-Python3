#!/bin/python3

import sys

if __name__ == '__main__':
    n = int(input().strip())
    
    # Convert to binary and split by '0' to get sequences of consecutive '1's
    binary_representation = bin(n)[2:]  # Convert to binary and remove the '0b' prefix
    max_consecutive_ones = max(map(len, binary_representation.split('0')))
    
    print(max_consecutive_ones)
