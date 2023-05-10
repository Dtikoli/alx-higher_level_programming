#!/usr/bin/python3
for n in range(0, 90):
    if n / 10 < n % 10:
        if n != 89:
            print(f"{n:02d}", end=", ")
print("89")
