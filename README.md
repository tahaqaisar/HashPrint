# HashPrint

## What's this?

***Note: this is a student project***

Surely a random string like ***'b318c90ba09d05dfc9ff3991974eee68'*** can look scary.
Be afraid no more, HashPrint got your back.

## About HashPrint

HashPrint is a forensic CLI tool that can identify which algorithm (like MD5, bcrypt, SHA256) produced the scary looking string, called a hash, like the above one.

## Features of HashPrint

1. **Hash Support:** HashPrint can identify 90+ hashes.
2. **Export Options:** HashPrint allows you to export results in various formats, like JSON and YAML.
3. **Multiple Hashes:** HashPrint can read multiple hashes from a text file. It can recursively scan a directory to locate text files that contain hashes. It can also accept multiple hashes from the command-line.
4. **Coloured Output:** HashPrint outputs coloured results, making them easier to read.
5. **Easy to use:** if you ever feel stuck, remember help is just a flag away.

## Installation

***Requires Python 3.14+***

If installing with pip, then you must have Python 3.14 or higher installed on your system

```console
$ pip install pyhashprint
```

**OR with uv**

uv installs the correct Python version if necessary

**First setup a virtual environment:**

```console
$ uv venv
```

**Then install:**

```console
$ uv pip install pyhashprint
```

**Use without installing**

***Requires uv***

```console
$ uv tool run pyhashprint
```

**OR**

```console
$ uvx pyhashprint
```

## How to use HashPrint?

| Option | Purpose |
|:------:|:-------------|
*-h*, *--help* | shows the help message and exits. |
*-f*, *--hash-file* | this option takes a path to a text file as an argument. With this option, HashPrint will read the file at the specified path for hashes. The file must contain one hash per line. |
*-c*, *--hash* | this option takes a hash as an argument and identifies it. It should be between single quotes and without the 0x prefix. |
*-x*, *--format* | this option lets you choose between the export formats. You can export the results in JSON, YAML and text formats. This option cannot work without the *-p*, *--path* option. |
*-p*, *--path* | this option specifies the path of the export file. If a path to a pre-existing file is specified, it will be overwritten if it already contains content. If the file at the specified path does not exist, HashPrint will create it. |
*-w*, *--walk* | this option recursively scans a directory at the specified path for text files, containing one hash per line. |
*-v*, *--version* | this option displays the version number of HashPrint. |

## Usage examples

**For help**

```console
$ hashprint --help
```

**Display the version number**

```console
$ hashprint --version
```

**Identify a single hash**

```console
$ hashprint -c 'a9993e364706816aba3e25717850c26c9cd0d89d'
```

OR

```console
$ hashprint --hash 'a9993e364706816aba3e25717850c26c9cd0d89d'
```

**Identify multiple hashes**

```console
$ hashprint -c '0cc175b9c0f1b6a831c399e269772661' -c 'e8b7be43'
```

**Identify hashes from a file + export results to a file**

```console
$ hashprint -f path/to/txt/file/containing/hashes -x text -p path/of/export/file
```

The above command exports results in a human readable text format at a file of your choice. HashPrint will create the file if it does not exist.

**Recursive Directory Scanner + exporting results to a file**

```console
$ hashprint -w path/to/directory -x format -p path/of/export/file
```

## LICENSE

[MIT](./LICENSE)
