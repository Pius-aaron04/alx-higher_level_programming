#!/usr/bin/python3
for i in range(100):
    if i != 99:
        print("{i:02d}".format(i=i), end=", ")
    else:
        print("{i}".format(i=i), end="\n")
