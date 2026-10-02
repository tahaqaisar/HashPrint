# In the Name of God, the Most Compassionate, Most Merciful


import os
from HashPrint.cli import console


def is_probably_text_file(file_path, sample_size=1024):
    try:
        with open(file_path, "rb") as file:
            sample = file.read(sample_size)
        if b"\00" in sample:
            console.print(
                f"[warning]Warning: file at path: '{file_path}' skipped - has .txt extensions but appears to be binary[/warning]"
            )
            return False
    except PermissionError:
        console.print("[error]Error: [/error]")
        return False
    except OSError as exception:
        console.print(f"[error]Error: something went wrong - {exception}[/error]")
        return False
    return True


def walker(start_dir):
    text_files = []
    for directory_root, _, files in os.walk(start_dir):
        for file in files:
            if file.endswith(".txt"):
                file_path = os.path.join(directory_root, file)
                if is_probably_text_file(file_path):
                    text_files.append(file_path)
    return text_files
