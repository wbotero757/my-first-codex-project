#!/usr/bin/env python3
"""Create Dropbox file requests from a CSV file."""

import csv
import os
import sys

try:
    import dropbox
except ImportError as e:
    print("dropbox package is required. Install with 'pip install dropbox'.")
    raise

ACCESS_TOKEN = os.environ['DROPBOX_ACCESS_TOKEN']


def create_file_requests(csv_path: str) -> None:
    """Create Dropbox file requests defined in a CSV file."""
    dbx = dropbox.Dropbox(ACCESS_TOKEN)

    with open(csv_path, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            title = row.get('title') or row.get('Title')
            destination = row.get('destination') or row.get('Destination')
            if not title or not destination:
                print(f"Skipping incomplete row: {row}")
                continue
            res = dbx.file_requests_create(title, destination)
            print(f"Created file request '{title}': {res.url}")


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print(f"Usage: {argv[0]} <path_to_csv>")
        return 1
    csv_path = argv[1]
    create_file_requests(csv_path)
    return 0


if __name__ == '__main__':
    raise SystemExit(main(sys.argv))
