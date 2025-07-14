# my-first-codex-project

One Click File Request to Dropbox from CSV

## Setup

1. Install dependencies:
   ```bash
   pip install dropbox
   ```
2. Set the environment variable `DROPBOX_ACCESS_TOKEN` with your Dropbox API token. You can create a `.env` file by copying `.env.example`:
   ```bash
   cp .env.example .env
   # edit .env and fill in your token
   ```

## Usage

Run the script and pass the path to your CSV file:

```bash
python dropbox_file_request.py requests.csv
```

The CSV must have `title` and `destination` columns describing the file request title and the destination folder in your Dropbox.
