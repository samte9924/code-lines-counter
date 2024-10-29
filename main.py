import os


# Content indentation
def add_tabulation(depth):
    return "|\t" * depth


def is_file(element):
    return os.path.isfile(element)


def is_directory(element):
    return os.path.isdir(element)


# Open a file and count each line that is empty or contains only spaces
def read_file(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            counter = 0
            for line in file:
                if not line.strip():
                    counter += 1
            return counter
    except FileNotFoundError:
        print("File not found.")
        return 0
    except PermissionError:
        print("You don't have the permission needed to access the file.")
        return 0
    except UnicodeDecodeError:
        print("File decoding error.")
        return 0


# Recursive function to read all files inside folders
def read_all_files_inside_folder(folder, depth=0):
    total = 0
    folder_name = os.path.basename(folder)
    print(f"{add_tabulation(depth)}{folder_name}/")

    # List containing all files and folders names
    folder_contents = os.listdir(folder)
    for index, element in enumerate(os.listdir(folder)):
        complete_path = os.path.join(folder, element)
        # check if the current element is the last inside its folder
        is_last = index == len(os.listdir(folder)) - 1

        if is_file(complete_path):
            file_lines = read_file(complete_path)
            total += file_lines
            prefix = "└──" if is_last else "├──"
            print(f"{add_tabulation(depth + 1)}{prefix} {element} - {file_lines} lines")
        elif is_directory(complete_path):
            subtotal = read_all_files_inside_folder(complete_path, depth + 1)
            total += subtotal
            if len(folder_contents) > 1 or depth > 0:
                print(f"{add_tabulation(depth + 2)}Subtotal for [{element}]: {subtotal} lines")

    return total


if __name__ == '__main__':
    path_in = input("> ")
    total_lines = read_all_files_inside_folder(path_in)
    print(f"\nTotal line across all files: {total_lines}")
