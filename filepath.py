import os

# Replace 'filename.txt' with name of file
file_name = 'filename.txt'

# Get the current working directory
current_directory = os.getcwd()

# Create full path to the file
file_path = os.path.join(current_directory, file_name)

print(f"The path to '{file_name}' is: {file_path}")
