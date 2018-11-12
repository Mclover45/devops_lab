b = int(input())
if 0 <= b <= 99:
    for i in range(b):
        print('%5s %6s %7s %8s' % ((i), oct(i), hex(i), bin(i)))
else:
    print("End")
