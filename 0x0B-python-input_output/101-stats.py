#!/usr/bin/python3
"""
A script that reads stdin line by line and computes metrics
"""


count = {}
sizes = 0
i = 0
for line in sys.stdin:
    i += 1
    line = line.split()
    status = line[-2]
    size = line[-1]
    if status in counts:
        count[status] += 1
    else:
        count[status] = 1
    sizes += int(size)
    if i % 10 = 0
    print("File size: {}".format(sizes))
    for code in sorted(counts.keys()):
        print("{}: {}".format(code, counts[code]))
try:
    while True:
        pass
except KeyboardInterrupt:
    print("File size: {}".format(sizes))
    for code in sorted(counts.keys()):
        print("{}: {}".format(code, counts[code]))
