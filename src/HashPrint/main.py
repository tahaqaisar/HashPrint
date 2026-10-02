# In the Name of God, the Most Compassionate, Most Merciful


import sys
from HashPrint.cli import (
    cli_parser,
    console,
    hint_line,
    DISCLAIMER_MESSAGE,
    POSSIBILITY_MESSAGE,
    SUCCESS_MESSAGE,
    print_banner,
)
from HashPrint.validator import validate
from HashPrint.identifier import identify
from HashPrint.printer import print_results_to_console
from HashPrint.reader import read_hashes
from HashPrint.walker import walker
from HashPrint.formatter import (
    write_text,
    write_json,
    write_yaml,
    format_data,
)
from HashPrint import __version__, __project_name__

EXIT_SUCCESS = 0
EXIT_GENERAL_ERROR = 1
EXIT_USAGE_ERROR = 2

WRITERS = {
    "text": write_text,
    "json": write_json,
    "yaml": write_yaml,
}


def main():
    args = cli_parser()
    candidate_hash_values_data = []
    results = []

    input_option_count = sum(
        [bool(args.candidate_hash), bool(args.hash_file), bool(args.walk)]
    )

    if input_option_count > 1:
        console.print(
            f"[error]\nError: only one input option (--hash --hash-file --walk) can be used at a time[/error]"
        )
        console.print(f"[hint]{hint_line}[/hint]")
        return EXIT_USAGE_ERROR

    print_banner()

    if args.version:
        console.print(f"[description]{__project_name__} v{__version__}[/description]")
        return EXIT_SUCCESS

    # args.candidate_hash is a list
    if args.candidate_hash:
        for candidate_hash in args.candidate_hash:
            candidate_hash_values_data.append(
                {"Hash": candidate_hash, "Source": "command-line"}
            )
    # args.hash_file is also a list
    elif args.hash_file:
        for hash_file in args.hash_file:
            file_hashes = read_hashes(hash_file)
            for file_hash in file_hashes:
                candidate_hash_values_data.append(
                    {"Hash": file_hash, "Source": hash_file}
                )
    elif args.walk:
        text_files = walker(args.walk)
        if not text_files:
            console.print(
                "[error]Error: no text (.txt) files found in the given directory[/error]"
            )
            return EXIT_GENERAL_ERROR
        for text_file in text_files:
            text_file_hashes = read_hashes(text_file)
            for text_file_hash in text_file_hashes:
                candidate_hash_values_data.append(
                    {"Hash": text_file_hash, "Source": text_file}
                )

    for candidate_hash_info in candidate_hash_values_data:
        is_hash_valid, error_msg = validate(candidate_hash_info["Hash"])
        if not is_hash_valid:
            results.append(
                {
                    "Hash": candidate_hash_info["Hash"],
                    "Source": candidate_hash_info["Source"],
                    "Error": error_msg,
                    "Matches": [],
                }
            )
            continue
        matches = identify(candidate_hash_info["Hash"])
        results.append(
            {
                "Hash": candidate_hash_info["Hash"],
                "Source": candidate_hash_info["Source"],
                "Error": error_msg,
                "Matches": matches,
            }
        )

    if not args.path and args.format:
        console.print("[error]\nError: missing option: '--path'[/error]")
        console.print(f"[hint]{hint_line}[/hint]")
        return EXIT_USAGE_ERROR
    elif not args.format and args.path:
        console.print("[error]\nError: missing option: '--format'[/error]")
        console.print(f"[hint]{hint_line}[/hint]")
        return EXIT_USAGE_ERROR
    elif args.format and args.path:
        data = format_data(results)
        WRITERS[args.format](args.path, data)
        console.print(f"[success]\n{SUCCESS_MESSAGE}[/success]")
        console.print(
            f"[disclaimer]File is overwritten if it was not empty[/disclaimer]"
        )
        console.print(f"\n[disclaimer]DISCLAIMER: {DISCLAIMER_MESSAGE}[/disclaimer]")
        return EXIT_SUCCESS

    print_results_to_console(results, DISCLAIMER_MESSAGE, POSSIBILITY_MESSAGE)

    return EXIT_SUCCESS


if __name__ == "__main__":
    sys.exit(main())
