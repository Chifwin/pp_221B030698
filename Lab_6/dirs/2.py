import os


def func(path: str):
    print(path + " \t", end='')
    if os.access(path, os.F_OK):
        print(f"exist", end = ', ')
        if os.access(path, os.R_OK): print(f"readable", end = ', ')
        else: print(f"is not readable", end = ', ')
        
        if os.access(path, os.W_OK): print(f"writable", end = ', ')
        else: print(f"is not writable", end = ', ')
        
        if os.access(path, os.X_OK): print(f"executable")
        else: print(f"is not executable")
    else:
        print(f"doesn't exist")


if __name__ == "__main__":
    func(r"English.docx")
    func(r"Lab_4.7z")
    func(r"res.txt")
    func(r"res.trt")