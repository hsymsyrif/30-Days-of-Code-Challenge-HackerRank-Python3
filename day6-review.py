#!/bin/python3

if __name__ == '__main__':
    t = int(input().strip())  # Read the number of test cases
    
    for _ in range(t):
        s = input().strip()  # Read the input string
        
        even_chars = s[0::2]  # Characters at even indices
        odd_chars = s[1::2]   # Characters at odd indices
        
        print(even_chars, odd_chars)
