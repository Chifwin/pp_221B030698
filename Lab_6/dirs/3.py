import os


def func(path: str):
    if os.access(path, os.F_OK):
        directory = "\\".join(path.split("\\")[:-1])
        print("Directory:", (directory if directory else "Nothing"))
        filename = path.split("\\")[-1]
        print("Filename: ", (filename if filename else "Nothing"))
    else:
        print(f"Path doesn't exist")


if __name__ == "__main__":
    func(r"C:\Users\osmer\Desktop\KBTU\English.docx")
    func(r"Lab_4.7z")
    func(r"res.txt")