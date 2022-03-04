from math import pi, tan


num = int(input("Input number of sides: "))
lenght = int(input("Input the length of a side: "))
print(f"The area of the polygon is: {num*lenght**2/4/tan(pi/num):.6}")