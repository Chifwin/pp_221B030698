def histogram(numbers: list):
    for i in numbers:
        print('*'*i)

if __name__ == "__main__":
    tests = ([4, 9, 7], [1, 2, 3], [7, 8, 9, 10, 5],)
    func_name = "histogram"
    for test in tests:
        print(f'Test {func_name}({test}) ->', eval(f"{func_name}({str(test)})"))
