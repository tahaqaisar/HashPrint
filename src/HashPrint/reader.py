# In the Name of God, the Most Compassionate, Most Merciful


from HashPrint.cli import console


def read_hashes(file_path):
    try:
        with open(file_path, "r") as hash_file:
            for line in hash_file:
                stripped_line = line.strip()
                if stripped_line:
                    yield stripped_line
    except FileNotFoundError:
        console.print(
            f"[error]Error: file at the path: '{file_path}' not found - please check the path[/error]"
        )
    except PermissionError:
        console.print(
            f"[error]Error: read permission to the path: '{file_path}' denied[/error]"
        )
    except IsADirectoryError:
        console.print(
            f"[error]Error: the path: '{file_path}' is a directory not a file[/error]"
        )
    except OSError as exception:
        console.print(
            f"[error]Error: cannot write to the path: '{file_path}' - {exception}[/error]"
        )
