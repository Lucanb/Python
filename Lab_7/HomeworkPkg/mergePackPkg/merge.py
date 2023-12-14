def merge_files(file_paths, output_path, separator='\n'):
    """
    Merge multiple text files into one.

    Parameters:
    - file_paths: List of paths to the text files in the desired order.
    - output_path: Path to the output merged file.
    - separator: Custom separator between file contents (default is newline).
    """
    with open(output_path, 'w') as output_file:
        for file_path in file_paths:
            with open(file_path, 'r') as input_file:
                output_file.write(input_file.read())
                output_file.write(separator)