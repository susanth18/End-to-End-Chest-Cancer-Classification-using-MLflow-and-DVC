import zipfile
import os

def unzip_file(zip_filepath, extract_to):
    """
    Unzips a zip file to the specified directory.

    :param zip_filepath: Path to the zip file to be extracted.
    :param extract_to: Directory where the contents will be extracted.
    """
    # Ensure the extraction directory exists
    os.makedirs(extract_to, exist_ok=True)

    # Open the zip file in read mode
    with zipfile.ZipFile(zip_filepath, 'r') as zip_ref:
        # Extract all contents into the specified directory
        zip_ref.extractall(extract_to)
        print(f"Files extracted to: {extract_to}")

# Example usage
if __name__ == "__main__":
    # Specify the path to the zip file and the extraction directory
    zip_filepath = "artifacts\data_ingestion\data.zip"  # Replace with your zip file path
    extract_to = "artifacts\data_ingestion"  # Replace with your desired extraction directory

    # Call the function to unzip the file
    unzip_file(zip_filepath, extract_to)