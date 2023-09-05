#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        if i == j or j < i:
            continue
        if i != 8 or j != 9:
            print(f"{i}{j}", end=", ")
        else:
            print(f"{i}{j}", end="\n")
