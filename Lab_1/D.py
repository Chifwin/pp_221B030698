from traceback import print_tb


num = int(input())
z = input()
if z == "k":
    print(f"{(num/1024):.{int(input())}f}")
else:
    print(num*1024)