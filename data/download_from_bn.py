import subprocess

# URL of the file or webpage you want to download
url = "https://example.com/file.zip"
url = "https://data.binance.us/public_data/spot/daily/klines/BNBUSDT/12h/BNBUSDT-12h-2023-01-01.zip"

# Output filename (optional)
output_filename = "downloaded_file.zip"

# Run wget command using subprocess
subprocess.run(["wget", "-O", output_filename, url])


import subprocess

# URL of the file you want to download
url = "https://data.binance.us/public_data/spot/daily/klines/BNBUSDT/12h/BNBUSDT-12h-2023-01-01.zip"

# Output filename
output_filename = "BNBUSDT-12h-2023-01-01.zip"

# Run curl command using subprocess
subprocess.run(["curl", "-s", url, "-o", output_filename])



import zipfile

# Path to the zip file
zip_path = "BNBUSDT-12h-2023-01-01.zip"

# Directory to extract the contents
extract_dir = "extracted_data"

# Open the zip file
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    # Extract all the contents of the zip file to the specified directory
    zip_ref.extractall(extract_dir)

print("Zip file extracted successfully!")