def to_centigrade(t: float):
    return (t - 32)*5/9

if __name__ == "__main__":
    far = float(input())
    print(f"{far} F is {to_centigrade(far):.3} C")
