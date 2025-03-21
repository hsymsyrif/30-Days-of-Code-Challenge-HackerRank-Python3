#!/bin/python3

import sys

def hourglass_sum(arr):
    max_sum = -sys.maxsize  # Initialize with the smallest possible integer

    for i in range(4):  # Row index
        for j in range(4):  # Column index
            # Compute the hourglass sum
            current_sum = (
                arr[i][j] + arr[i][j+1] + arr[i][j+2] +
                arr[i+1][j+1] +
                arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            )

            # Update max_sum if the current_sum is greater
            max_sum = max(max_sum, current_sum)

    return max_sum

if __name__ == '__main__':
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglass_sum(arr)
    print(result)
