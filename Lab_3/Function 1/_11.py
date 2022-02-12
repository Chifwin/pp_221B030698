def is_palindrome(s: str):
    return s == s[::-1]

if __name__ == "__main__":
    tests = ("madam", "fdsf", "asdsa", "asddsa")
    func_name = "is_palindrome"
    for test in tests:
        print(f'Test {func_name}({test}) ->', eval(f"{func_name}('{test}')"))
