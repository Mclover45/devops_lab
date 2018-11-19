def polin(b):
    c = b[::-1]
    if b == c:
        b = True
    else:
        b = False
    return(b)

if __name__ == '__main__':
    b = (input("Input number:"))
    polin(b)
