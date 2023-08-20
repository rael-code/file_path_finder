import os

# Replace 'filename.txt' with the name of your file
file_name = 'filename.txt'

# Get the current working directory
current_directory = os.getcwd()

# Construct the full path to the file
file_path = os.path.join(current_directory, file_name)

print(f"The path to '{file_name}' is: {file_path}")
