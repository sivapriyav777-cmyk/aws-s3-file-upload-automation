import os

def validate_file(file_path):

    if not os.path.exists(file_path):
        raise FileNotFoundError("File does not exist")

    if not os.path.isfile(file_path):
        raise ValueError("Path is not a file")

    if os.path.getsize(file_path) == 0:
        raise ValueError("File is empty")

    if not file_path.lower().endswith(".csv"):
        raise ValueError("Only CSV files are allowed")

    return True
