def fibonacci(limit):
    fibonacci_list = [0, 1]  # Array starts with 0 and 1
    while fibonacci_list[-1] + fibonacci_list[-2] < limit:
        next_value = fibonacci_list[-1] + fibonacci_list[-2]
        fibonacci_list.append(next_value)
    return fibonacci_list

# Get limit from user
def main():
    try:
        limit = int(input("Fibonacci dizisinin üst limitini girin: "))
        if limit < 0:
            print("Lütfen pozitif bir sayı girin.")
        else:
            fib_series = fibonacci(limit)
            print(f"Fibonacci dizisi {limit} sayısına kadar: {fib_series}")
    except ValueError:
        print("Lütfen geçerli bir tam sayı girin.")

# Start the main function
if __name__ == "__main__":
    main()
