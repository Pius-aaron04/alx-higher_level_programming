#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        if i == j or j < i:
            continue
        if i != 8 or j != 9:
            print("{i}{j}".format(i=i, j=j), end=", ")
        else:
            print("{i}{j}".format(i=i, j=j), end="\n")
