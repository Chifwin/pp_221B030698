def spy_game(nums: list):
    if nums.count(0) >= 2 and 7 in nums and \
        nums.index(0, nums.index(0)+1) < nums.index(7):
        return True
    return False

if __name__ == "__main__":
    tests = (
        "spy_game([1,2,4,0,0,7,5])",
        "spy_game([1,0,2,4,0,5,7])",
        "spy_game([1,7,2,0,4,5,0])"
    )
    for test in tests:
        print(f"Test {test} -> {eval(test)}")
