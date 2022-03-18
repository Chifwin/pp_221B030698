import os


def func(path: str):
    if os.path.isfile(path=path):
        try:
            os.remove(path)
            print(f"{path} have deleted")
        except PermissionError:
            print(f"Can not get access to the {path}")
    else:
        print(f"{path} doesn't exist")


if __name__ == "__main__":
    func(r"sample-data2.json")
    func(r"sample-data2.json")
    func(r"C:\devlist.txt")