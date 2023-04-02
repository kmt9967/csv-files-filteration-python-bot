import os

folder_path = input("Enter the path of the folder: ")

try:
    for filename in os.listdir(folder_path):
        if filename.endswith('.csv'):
            if any(char in filename for char in ['á', 'é', 'í', 'ó', 'ú', 'ç', 'â', 'Á']):
                new_name = filename.replace('á', '').replace('é', '').replace('í', '').replace('ó', '').replace('ú', '').replace('ç', '').replace('â', '').replace('Á', '').replace('Ç', '').replace('Â', '')
                os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_name))
                print(f'Renamed file: {filename} --> {new_name}')
            else:
                print(f'No relevant characters found in filename: {filename}')
        else:
            print(f'File is not a CSV: {filename}')
except OSError as e:
    print(f'Error: {e}')
else:
    print('All files renamed successfully.')
