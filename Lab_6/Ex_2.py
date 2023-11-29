import os
import sys

def rename_files(directory_path):
    try:
        if not os.path.isdir(directory_path):
            raise ValueError("This directory path doesn't exists")

        files = os.listdir(directory_path) 
        for index,file_name in enumerate(files):
             extension = os.path.splitext(file_name)[1]
             new_filename = f"file{index}{os.path.splitext(file_name)[0]}"
            #  new_filename = f"file{index}"
            #  new_filename = f"{index}{os.path.splitext(file_name)[0]}"
            #  new_filename = f"{os.path.splitext(file_name)[0]}{index}"
             new_filename += extension
             print(new_filename)   
             old_path = os.path.join(directory_path, file_name)
             new_path = os.path.join(directory_path, new_filename)
             try:
                os.rename(old_path, new_path)
                print(f"File '{file_name}' successfully renamed to '{new_filename}'.")
             except FileNotFoundError:
                print(f"Error: File '{file_name}' not found.")
             except FileExistsError:
                print(f"Error: File '{new_filename}' already exists.")
    
    except ValueError as valueError:
        print(f"Invalid directory path: {valueError}")
    except Exception as error:
        print(f"An error occurred: {error}")


if __name__ == '__main__':
      if len(sys.argv) != 2:
            print("false")
      else:
       p0=sys.argv[1]
       rename_files(p0)              