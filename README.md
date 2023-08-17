# File-organizer
This Python script is designed to organize files with the same extension from your Downloads directory into a destination directory. It uses the os and shutil modules to achieve this functionality.
# How it works
1. The script starts by importing the necessary modules: os and shutil.

2. The source directory (downloads_dir) is set to your Downloads directory, and the destination directory (dest_dir) is set to a location where you want to move the ".rar" files.

3. The script then checks if the destination directory doesn't exist. If it doesn't, it creates the directory.

4. The script iterates through each file in the Downloads directory using os.listdir(downloads_dir).

5. For each file, it checks if the file ends with ".rar", indicating that it's a rar archive.

6. If the file is indeed a ".rar" archive, it constructs the full source path and destination path using os.path.join().

7. It then uses shutil.move() to move the file from the Downloads directory to the destination directory.

8. After moving the file, it prints a message indicating which file was moved to which directory.
