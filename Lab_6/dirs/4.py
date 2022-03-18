def func(path: str):
    with open(path, "r", encoding="utf-8") as file:
        s = file.read()
        return s.count('\n') + (1 if s[-1] != '\n' else 0)


if __name__ == "__main__":
    print(func(r"C:\TMP\sample-data.json"))