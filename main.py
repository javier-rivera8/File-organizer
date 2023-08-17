import os
import shutil

# Define the source and destination directories of files
downloads_dir = os.path.expanduser("~/Downloads")
dest_dir = os.path.expanduser("~/Documents/ALLRAR")

# Create the destination directory if it doesn't exist
if not os.path.exists(dest_dir):
    os.mkdir(dest_dir)

# Iterate over all the files in the Downloads directory
for filename in os.listdir(downloads_dir):
    # Check if the file is a zip archive
    if filename.endswith(".rar"):
        # Construct the source and destination paths
        src_path = os.path.join(downloads_dir, filename)
        dest_path = os.path.join(dest_dir, filename)
        # Move the file to the destination directory
        shutil.move(src_path, dest_path)
        print(f"Moved {filename} to {dest_dir}")
    