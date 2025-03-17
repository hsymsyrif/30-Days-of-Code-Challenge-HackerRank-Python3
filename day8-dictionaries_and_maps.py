import sys

def phone_book():
    n = int(input().strip())  # Read the number of entries
    phone_dict = {}
    
    # Reading phone book entries
    for _ in range(n):
        name, number = input().strip().split()
        phone_dict[name] = number
    
    # Reading queries
    for query in sys.stdin:
        query = query.strip()
        if query in phone_dict:
            print(f"{query}={phone_dict[query]}")
        else:
            print("Not found")

if __name__ == "__main__":
    phone_book()
