# In the Name of God, the Most Compassionate, Most Merciful


from HashPrint.cli import console, DISCLAIMER_MESSAGE, SUCCESS_MESSAGE
from HashPrint import __project_name__, __version__
from datetime import datetime
import json
import yaml

timestamp = datetime.now()
formatted_timestamp = timestamp.strftime("%Y-%m-%d %H:%M:%S")


def format_data(results):
    data = [
        {
            "timestamp": f"{formatted_timestamp} by {__project_name__} v{__version__}",
            "success": SUCCESS_MESSAGE,
            "disclaimer": DISCLAIMER_MESSAGE,
        }
    ]
    for result in results:
        info = {
            "Hash": result["Hash"],
            "Source": result["Source"],
            "Possible Algorithms": [
                {
                    "Name": algorithm.name,
                    "Family": algorithm.family,
                    "Popularity Score": algorithm.popularity,
                }
                for algorithm in result["Matches"]
            ],
            "Error": result["Error"],
        }
        data.append(info)
    return data


def write_text(file_path, data):
    try:
        with open(file_path, "w", encoding="utf-8") as text_file:
            text_file.write(f"Generated at: {formatted_timestamp} by {__project_name__} v{__version__}\n")
            text_file.write(f"{SUCCESS_MESSAGE}\n")
            text_file.write(f"DISCLAIMER: {DISCLAIMER_MESSAGE}\n\n")
            for result in data[1:]:
                text_file.write(f"Source: {result["Source"]}\n")
                text_file.write(f"Hash: '{result["Hash"]}'\n")
                if not result["Possible Algorithms"]:
                    text_file.write("Possible Algorithms: None\n")
                else:
                    text_file.write("Possible Algorithms:\n")
                    for algorithm in result["Possible Algorithms"]:
                        text_file.write(f"[#] Name: {algorithm["Name"]}\n")
                        text_file.write(f"\t[-] Family: {algorithm["Family"]}\n")
                if not result["Error"]:
                    text_file.write("Error: None\n\n")
                else:
                    text_file.write(f"Error: {result["Error"]}\n\n")
    except FileNotFoundError:
        console.print(
            f"[error]\nError: a directory in the path: '{file_path}' does not exist\n[/error]"
        )
    except PermissionError:
        console.print(
            f"[error]\nError: write permission to the path: '{file_path}' denied\n[/error]"
        )
    except IsADirectoryError:
        console.print(
            f"[error]\nError: the path: '{file_path}' is a directory not a file\n[/error]"
        )
    except OSError as exception:
        console.print(
            f"[error\n]Error: cannot write to the path: '{file_path}' - {exception}\n[/error]"
        )


def write_json(file_path, data):
    try:
        with open(file_path, "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=2)
    except FileNotFoundError:
        console.print(
            f"[error]\nError: a directory in the path: '{file_path}' does not exist\n[/error]"
        )
    except PermissionError:
        console.print(
            f"[error]\nError: write permission to the path: '{file_path}' denied\n[/error]"
        )
    except IsADirectoryError:
        console.print(
            f"[error]\nError: the path: '{file_path}' is a directory not a file\n[/error]"
        )
    except OSError as exception:
        console.print(
            f"[error]\nError: cannot write to the path: '{file_path}' - {exception}\n[/error]"
        )


def write_yaml(file_path, data):
    try:
        with open(file_path, "w", encoding="utf-8") as yaml_file:
            yaml.dump(data, yaml_file, encoding="utf-8", sort_keys=False)
    except FileNotFoundError:
        console.print(
            f"[error]\nError: a directory in the path: '{file_path}' does not exist\n[/error]"
        )
    except PermissionError:
        console.print(
            f"[error]\nError: write permission to the path: '{file_path}' denied\n[/error]"
        )
    except IsADirectoryError:
        console.print(
            f"[error]\nError: the path: '{file_path}' is a directory not a file\n[/error]"
        )
    except OSError as exception:
        console.print(
            f"[error]\nError: cannot write to the path: '{file_path}' - {exception}\n[/error]"
        )
