def TOH(n, A, B, C):
    if n == 1:
        print("move 1 from ", A, " to ", C)

    else:
        TOH(n-1, A,C,B)
        print("move ", n, " from ", A, "to", C)
        TOH(n-1, B,A,C)


print(TOH(3,'A', 'B', 'C'))