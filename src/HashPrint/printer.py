# In the Name of God, the Most Compassionate, Most Merciful


from HashPrint.cli import console


def print_results_to_console(results, DISCLAIMER_MESSAGE, POSSIBILITY_MESSAGE):
    for result in results:
        if not result["Error"]:
            if not result["Matches"]:
                console.print(f"[hint]\nSource: {result["Source"]}[hint]")
                console.print(f"[fail]Hash: '{result["Hash"]}'[/fail]")
                console.print("[fail]No algorithms produce the given hash[/fail]")
                console.print(f"[hint]Note: {POSSIBILITY_MESSAGE}[/hint]")
                continue
            console.print(f"[hint]\nSource: {result["Source"]}[/hint]")
            console.print(f"[information]Hash: '{result["Hash"]}'[/information]")
            console.print(f"[information]Possible Algorithms:\n[/information]")
            for algorithm in result["Matches"]:
                console.print(f"[success]\\[#] {algorithm.name}[/success]")
                console.print(f"[success]\tFamily: {algorithm.family}[/success]")
        else:
            console.print(f"[hint]\nSource: {result["Source"]}[/hint]")
            console.print(f"[error]Hash: '{result["Hash"]}'[/error]")
            console.print(f"[error]Error: {result["Error"]}[/error]")
    console.print(f"[disclaimer]\nDISCLAIMER: {DISCLAIMER_MESSAGE}[/disclaimer]")
