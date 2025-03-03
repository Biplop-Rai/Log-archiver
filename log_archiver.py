import os
import sys
import tarfile
from datetime import datetime

# Function to create a timestamped filename
def generate_timestamped_filename():
    now = datetime.now()
    return now.strftime("logs_archive_%Y%m%d_%H%M%S.tar.gz")

# Function to compress logs into a tar.gz file
def compress_logs(log_directory):
    if not os.path.isdir(log_directory):
        print(f"Error: The directory {log_directory} does not exist.")
        return
    
    # Generate the compressed filename
    archive_filename = generate_timestamped_filename()
    
    # Create the archive directory if it doesn't exist
    archive_dir = "archives"
    os.makedirs(archive_dir, exist_ok=True)

    # Path to the final compressed archive file
    archive_filepath = os.path.join(archive_dir, archive_filename)
    
    # Create the tar.gz archive
    with tarfile.open(archive_filepath, "w:gz") as tar:
        for root, dirs, files in os.walk(log_directory):
            for file in files:
                file_path = os.path.join(root, file)
                tar.add(file_path, arcname=os.path.relpath(file_path, log_directory))

    print(f"Logs have been compressed into: {archive_filepath}")
    
    # Log the date and time of the archive creation
    log_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("archive_log.txt", "a") as log_file:
        log_file.write(f"Archived logs from {log_directory} on {log_time}. Archive: {archive_filename}\n")

# Main function to parse command-line arguments
def main():
    if len(sys.argv) != 2:
        print("Usage: log-archive <log-directory>")
        sys.exit(1)
    
    log_directory = sys.argv[1]
    compress_logs(log_directory)

if __name__ == "__main__":
    main()

