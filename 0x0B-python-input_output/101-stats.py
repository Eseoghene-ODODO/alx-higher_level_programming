#!/usr/bin/python3
"""
A script the reads stdin line by line and computes metrics
"""

import sys
import signal


total_size = 0
counts = {}


def print_stats():
    """function body"""
    print(f"File size: {total_size}")
    sorted_counts = sorted(counts.items())
    for code, count in sorted_counts:
        print(f"{code}: {count}")


def handler(signum, frame):
    """function body"""
    print_stats()


signal.signal(signal.SIGINT, handler)

i = 0
for line in sys.stdin:
    i += 1
    if i % 10 == 0:
        print_stats()

    parts = line.split()
    # Convert code to string explicitly
    code = str(parts[-3])
    size = int(parts[-2])
    # Check if code is valid
    if code in counts:
        counts[code] += 1
    else:
        counts[code] = 1

    total_size += size

print_stats()
