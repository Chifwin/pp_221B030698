def unique_elements(l: list):
    res = []
    for i in l:
        if i not in res:
            res.append(i)
    return res

if __name__ == "__main__":
    tests = (
        "unique_elements([1, 2, 3, 1, 4, 5, 6])",
        "unique_elements(['jj', 'j', 'jj', 'k'])",
        "unique_elements([1.5, 1.2, 1.5, .5, 9.8])"
    )
    for test in tests:
        print(f"Test {test} -> {eval(test)}")
