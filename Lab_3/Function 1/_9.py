import math

def sphere_volume(r: float):
    return 4/3 * math.pi * r**3 

if __name__ == "__main__":
    tests = (
        "sphere_volume(1)",
        "sphere_volume(5)",
        "sphere_volume(4.45)"
    )
    for test in tests:
        print(f"Test {test} -> {eval(test)}")
