# Log Archiver Tool

This is a simple command-line tool for archiving logs. It allows you to compress log files in a directory into a `.tar.gz` archive and store the archive in a new directory. This helps in maintaining a clean system by compressing old logs for future reference.

## Features

- Accepts a log directory as an argument.
- Compresses logs in the directory into a `.tar.gz` file.
- Stores the compressed logs in an "archived_logs" directory.
- Logs the timestamp of the archive creation to a file (`archive_log.txt`).

## Requirements

- Python 3.x

## Installation

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/Biplop-Rai/log-archiver.git

## Usage
1,To run the tool and archive logs, use the following command:
- python log_archiver.py <log-directory>

##Example Output
-Logs have been compressed into: archives/logs_archive_20250303_183148.tar.gz

   
