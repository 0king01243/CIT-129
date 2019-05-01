# Breaks if you do not have a number

while True:
    try:
        A = int(input("Input the A value: "))
        B = int(input("Input the B value: "))
        C = A * B
        print(A, "*", B, "=", C)
    except ValueError:
        print("--Please input an int type value--")
    finally:
        print("--Next calculation will begin!--")

