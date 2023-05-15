#!/usr/bin/python3
print(", ".join("{:02d}".format(n) for n in range(90) if n / 10 < n % 10))
