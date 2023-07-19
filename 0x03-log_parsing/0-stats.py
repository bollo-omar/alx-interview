#!/usr/bin/python3
import sys

def print_statistics(total_file_size, status_code_counts):
    print("File size:", total_file_size)
    for code, count in status_code_counts.items():
        print(f"{code}: {count}")

def main():
    total_file_size = 0
    status_code_counts = {}

    try:
        for i, line in enumerate(sys.stdin, start=1):
            try:
                _, _, _, _, _, status_code_str, file_size_str = line.strip().split()
                status_code = int(status_code_str)
                file_size = int(file_size_str)

                total_file_size += file_size
                status_code_counts[status_code] = status_code_counts.get(status_code, 0) + 1

                if i % 10 == 0:
                    print_statistics(total_file_size, status_code_counts)

            except ValueError:
                continue

    except KeyboardInterrupt:
        print_statistics(total_file_size, status_code_counts)
        sys.exit(0)

if __name__ == "__main__":
    main()

