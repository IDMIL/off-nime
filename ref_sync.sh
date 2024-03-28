#!/bin/bash

# Define the source file path and the target directory path
source_file_path="ISIDM/sorted_references.xlsx"
target_directory_path="/Users/miu/Library/CloudStorage/GoogleDrive-maxwiththehax@gmail.com/My Drive"

# Move the file to the target directory
cp "$source_file_path" "$target_directory_path"

# Check if the move was successful
if [ $? -eq 0 ]; then
  echo "File has been successfully copied."
else
  echo "Failed to move the file."
fi
