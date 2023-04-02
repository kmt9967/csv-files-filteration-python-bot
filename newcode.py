import tkinter as tk
from tkinter import filedialog
import pandas as pd
import os

# Define the required columns
required_cols = ['name', 'fulladdress', 'email', 'phone 1', 'phone', 'business categories', 'count_reviews','count reviews',
                 'average_rating', 'average rating', 'latitude', 'longitude', 'website', 'google_maps_url', 'google maps_url', 'facebook_url',
                 'twitter_url', 'instagram_url', 'featured image', 'Country', 'City', 'COUNTRY', 'CITY']

# Ask user to select CSV files
root = tk.Tk()
root.withdraw()
file_paths = filedialog.askopenfilenames(filetypes=[('CSV files', '*.csv')])

# Create a new directory to save modified CSV files
if not os.path.exists('modified'):
    os.makedirs('modified')

# Initialize a list to keep track of files that have errors
error_files = []

# Loop over the selected CSV files
for file_path in file_paths:
    try:
        # Read the CSV file into a pandas DataFrame
        df = pd.read_csv(file_path)

        # Find any required columns that exist in the DataFrame
        matching_cols = [col for col in required_cols if col in df.columns]

        if 'featured image' not in df.columns:
            # If the featured image column doesn't exist, create a new one
            df.insert(14, 'featured image', '')

        if len(matching_cols) > 0:
            # Remove any columns that are not required
            df = df[matching_cols]

            # Save the modified DataFrame as a new CSV file
            file_name = os.path.basename(file_path)
            modified_file_path = os.path.join('modified', file_name)
            df.to_csv(modified_file_path, index=False)
        else:
            # If none of the required columns exist, print a warning message
            print(f'Warning: {file_path} does not contain any required columns')
            error_files.append(file_path)
    except:
        # If there's an error reading the file, print a warning message
        print(f'Error reading file: {file_path}')
        error_files.append(file_path)

# Print the list of files with errors, if any
if len(error_files) > 0:
    print('The following files were skipped due to errors:')
    for file_path in error_files:
        print(file_path)
