#!/usr/bin/python3
"""
A script the reads stdin line by line and computes metrics
"""

import sys
import signal 


total_size = 0
counts = {str(code): 0 for code in range(200, 506, 100)}

def print_stats():
    """function body"""
    global total_size, counts  
    print(f"File size: {total_size}")
    for code, count in sorted(counts.items()):
        if count > 0:
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

    # Print for debugging
    print(line) 
    print(parts)

    size = int(parts[-2])

    # Convert code to string explicitly 
    code = str(parts[-3])

    # Check if code is valid
    if code in counts:
        counts[code] += 1

    total_size += size

print_stats()
