import requests   # For sending HTTP requests to fetch the image
import os         # For creating folder (directory) and handling files
from urllib.parse import urlparse  # To extract filename from the URL

# Ask user for an image URL ======
url = input("Enter the image URL: ")

# Create 'Fetched_Images' directory if it doesn’t exist ======
folder_name = "Fetched_Images"
os.makedirs(folder_name, exist_ok=True)   # If folder exists, do nothing. Otherwise, create it.

# Extract filename from the URL
# Example: "https://example.com/pic.jpg" → "pic.jpg"
parsed_url = urlparse(url)   # Breaks the URL into parts (scheme, netloc, path, etc.)
filename = os.path.basename(parsed_url.path)   # Extracts the last part (e.g., "pic.jpg")

# If the URL does not have a valid filename, generate one
if not filename:
    filename = "downloaded_image.jpg"

# Full path to save the image
file_path = os.path.join(folder_name, filename)

# Try downloading the image
try:
    response = requests.get(url, stream=True)   # stream=True → fetch in chunks (useful for large files)

    # Check if request was successful (status code 200 = OK)
    response.raise_for_status()

    # Open file in binary write mode ("wb") and save the image
    with open(file_path, "wb") as f:
        for chunk in response.iter_content(1024):   # Write in chunks of 1024 bytes
            f.write(chunk)

    print(f"✅ Image saved successfully in '{file_path}'")

# ====== Step 6: Handle Errors Gracefully ======
except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")

except requests.exceptions.ConnectionError:
    print("Connection error. Please check your internet.")

except requests.exceptions.Timeout:
    print("Request timed out. Try again later.")

except requests.exceptions.RequestException as err:
    print(f"An error occurred: {err}")
