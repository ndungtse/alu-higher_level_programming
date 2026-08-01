#!/usr/bin/python3
"""Reads stdin line by line and computes HTTP log metrics."""
import sys


def print_stats(total_size, status_counts):
    """Print the accumulated file size and status code counts.

    Args:
        total_size: the running total of file sizes.
        status_counts: a dict mapping status codes to their counts.
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_counts):
        print("{}: {}".format(code, status_counts[code]))


if __name__ == "__main__":
    total_size = 0
    status_counts = {}
    valid_codes = {200, 301, 400, 401, 403, 404, 405, 500}
    line_count = 0

    try:
        for line in sys.stdin:
            parts = line.split()
            if len(parts) >= 2:
                try:
                    total_size += int(parts[-1])
                except ValueError:
                    pass
                try:
                    code = int(parts[-2])
                    if code in valid_codes:
                        status_counts[code] = status_counts.get(code, 0) + 1
                except ValueError:
                    pass
            line_count += 1
            if line_count % 10 == 0:
                print_stats(total_size, status_counts)
    except KeyboardInterrupt:
        print_stats(total_size, status_counts)
        raise
