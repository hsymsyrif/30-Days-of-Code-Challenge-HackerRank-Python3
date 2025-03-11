# Declare initial variables
initial_int = 4
initial_double = 4.0
initial_string = "HackerRank "

# Read inputs
user_int = int(input())
user_double = float(input())
user_string = input()

# Perform operations
sum_int = initial_int + user_int
sum_double = initial_double + user_double
concatenated_string = initial_string + user_string

# Print results
print(sum_int)
print(f"{sum_double:.1f}")
print(concatenated_string)
