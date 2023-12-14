import os
import sys
import glob

def read_files(directory_path, file_extension):
    try:
        if not os.path.isdir(directory_path):
            raise ValueError("This directory doesn't exist!")

        path = os.path.join(directory_path, f'*.{file_extension}')
        all_files = glob.glob(path)

        for file in all_files:
            try:
                with open(file, 'r') as f:
                    file_text = f.read()
                    print(f'File: {file} has content:\n{file_text}')
            except Exception as errorr:
                print(f"Error 1 at reading file {file}: {errorr}")
    except ValueError as valueError:
        print(f"Invalid directory path: {valueError}")
    except Exception as error2:
        print(f"An error 2 occurred: {error2}")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Write as parameters only <directory name> and <file extension>')
    else:
        p1 = sys.argv[1]
        p2 = sys.argv[2]
        read_files(p1, p2)
