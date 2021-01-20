def towers(top, frm, inter, to):
    if top == 1:
        print("disk 1 from " + frm + " to " + to)
    else:
        towers(top-1, frm, to, inter) # Process 1
        print("disk " + str(top) + " from " + frm + " to " + to)

        # Process 2
        towers(top-1, inter, frm, to) # Process 3

if __name__ == "__main__":
    num = 3
    towers(num, "A", "B", "C")