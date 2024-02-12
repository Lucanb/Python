import os
import sys

def count_file_extension(directory_name):
    try:
        if not os.path.isdir(directory_name):
            raise ValueError("No directory with this name")
        
        file_names = os.listdir(directory_name)
        print(file_names)
        
        if not file_names:
            raise ValueError("The directory is empty.")
        
        count_extension = {}

        for file_name in file_names:
            name, extension = os.path.splitext(file_name)
            extension = extension.lower()
            if extension not in count_extension:
                count_extension[extension] = 1
            else:
                count_extension[extension] += 1

        for element, count in count_extension.items():
            print(f"{element}: {count} file(s)")

    except ValueError as valueError:
        print(f"Wrong value: {valueError}")
    except Exception as error:
        print(f"Error: {error}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Wrong parameters, you need to put only a parameter with the directory path')
    else:
        p0 =  sys.argv[1]
        count_file_extension(p0)
