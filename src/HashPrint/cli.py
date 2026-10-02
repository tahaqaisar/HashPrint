# In the Name of God, the Most Compassionate, Most Merciful


import argparse
import pyfiglet
from rich_argparse import RichHelpFormatter
from rich.console import Console
from rich.theme import Theme
import sys
from HashPrint import __project_name__

DISCLAIMER_MESSAGE = "Hash identification is based on pattern matching - therefore some hashes cannot be identified with certainty"
POSSIBILITY_MESSAGE = "The string may not be a real hash"
SUCCESS_MESSAGE = f"{__project_name__} ran successfully"


class Parser(argparse.ArgumentParser):
    def error(self, message):
        console.print(f"[error]\nError: {message}[/error]")
        console.print(f"[hint]{hint_line}[/hint]")
        sys.exit()


def print_banner():
    banner = pyfiglet.figlet_format(__project_name__, font="slant")
    console.print(f"[banner]{banner}[/banner]")


theme = Theme(
    {
        "success": "#00A86B",  # Jade color
        "information": "#00D084",  # Bright Jade color
        "error": "bold #FF4A4A",  # Coral red color
        "fail": "#EC5B38",  # Warm orange-red color
        "hint": "#FF5FCF",  # Bright hot pink color
        "banner": "#499A13",  # Vida Loca color
        "description": "#24B1B1",  # Medium dark teal color
        "usage": "#2F2FE4",  # Electric blue color
        "disclaimer": "#B8860B",  # Dark goldenrod color
        "warning": "#FFFF00",  # Yellow color
    }
)

RichHelpFormatter.styles["argparse.args"] = "#03AED2"  # Sky blue color
RichHelpFormatter.styles["argparse.groups"] = "#FF6D1F"  # Bright orange color
RichHelpFormatter.styles["argparse.text"] = "#24B1B1"  # Medium dark teal color

console = Console(highlight=False, theme=theme)


description = "\nA forensic CLI tool for hash identification"
hint_line = "\nRun with -h for usage information"
program_name_cli = "hashprint"
format_choices = ["text", "json", "yaml"]


def cli_parser():
    if len(sys.argv) == 1:
        print_banner()
        console.print(f"[description]{description}[/description]")
        console.print(f"[hint]{hint_line}[/hint]")
        sys.exit()

    parser = Parser(
        prog=program_name_cli,
        description=description,
        formatter_class=RichHelpFormatter,
        color=False,
    )
    parser.add_argument(
        "-f",
        "--hash-file",
        action="append",
        help="path to a text (.txt) file containing one hash per line",
    )
    parser.add_argument(
        "-c",
        "--hash",
        dest="candidate_hash",
        action="append",
        help="hash to identify between single quotes and without the 0x prefix",
    )
    parser.add_argument("-x", "--format", choices=format_choices, help="output format")
    parser.add_argument(
        "-p",
        "--path",
        metavar="PATH",
        help="path of the output file - overwrites the file if it is not empty",
    )
    parser.add_argument(
        "-w",
        "--walk",
        metavar="PATH",
        help="recursively scans a directory for text (.txt) files - containing one hash per line",
    )
    parser.add_argument(
        "-v", "--version", action="store_true", help="displays the version number"
    )
    args = parser.parse_args()
    return args
