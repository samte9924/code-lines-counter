import os


# Returns a string of tabulation based on the current depth.
def add_tabulation(depth):
    return "|\t" * depth


# Opens a file and counts each line that not empty or contains only spaces.
def read_file(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            return sum(1 for line in file if line.strip())
    except FileNotFoundError:
        print("File not found.")
        return 0
    except PermissionError:
        print("You don't have the permission needed to access the file.")
        return 0
    except UnicodeDecodeError:
        print("File decoding error.")
        return 0


# Recursively reads all files in the selected folder using a DFS algorithm and prints the total lines.
def read_all_files_inside_folder(folder, depth=0):
    total = 0
    folder_name = os.path.basename(folder)
    print(f"{add_tabulation(depth)}{folder_name}/")

    # Convert iterator to a list
    with os.scandir(folder) as it:
        folder_contents = list(it)

    for index, entry in enumerate(folder_contents):
        # Check if the current entry is last in the folder
        is_last = index == len(folder_contents) - 1

        if entry.is_file():
            file_lines = read_file(entry.path)
            total += file_lines
            prefix = "└──" if is_last else "├──"
            print(f"{add_tabulation(depth + 1)}{prefix} {entry.name} - {file_lines} lines")

        elif entry.is_dir():
            subtotal = read_all_files_inside_folder(entry.path, depth + 1)
            total += subtotal
            print(f"{add_tabulation(depth + 2)}Subtotal for [{entry.name}]: {subtotal} lines")

    return total


if __name__ == '__main__':
    path_in = input("> ")
    total_lines = read_all_files_inside_folder(path_in)
    print(f"\nTotal line across all files: {total_lines}")
