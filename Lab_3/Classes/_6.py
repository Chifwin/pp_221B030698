def filter_prime_numbers(numbers: list):
    return list(filter(lambda x: x > 1 and not any((x%i == 0 for i in range(2, int(x**0.5) + 1))), numbers))

if __name__ == "__main__":
    #[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    print(filter_prime_numbers([i for i in range(50)]))