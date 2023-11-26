import os
import sys


def calculate_folder_size(director_name):
    try:
        if not os.path.isdir(director_name):
            raise ValueError("This directory path doesn't exists")

        size_total = 0

        for folder_name, subfolders_name, file_names in os.walk(director_name):    
             for file_name in file_names:
                file_path = os.path.join(folder_name, file_name)
                try:
                    file_size = os.path.getsize(file_path)
                    print(f"file_name : {file_name} , size : {file_size}")
                    size_total += file_size
                except Exception as error:
                    print(f"Error at getting file size {file_path} : {error}")

        print(f"Total folder size for '{director_name}': {size_total} bytes")

    except ValueError as valueError:
        print(f"Wrong directory path: {valueError}")

    except Exception as error:
        print(f"Error: {error}")
    
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Please insert as parameeter the path of directory')
    else:
        p0=sys.argv[1]
        size = calculate_folder_size(p0)
        print(size)