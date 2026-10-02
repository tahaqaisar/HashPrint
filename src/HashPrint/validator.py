# In the Name of God, the Most Compassionate, Most Merciful


def validate(raw_hash):
    INVALID = {
        "!",
        "@",
        "#",
        "%",
        "^",
        "&",
        "(",
        ")",
        "[",
        "]",
        "'",
        '"',
        "<",
        ">",
        ";",
        ":",
        "\\",
    }
    cleaned_hash = raw_hash.strip()
    if not cleaned_hash:
        return False, "hash is empty"
    for char in cleaned_hash:
        if char.isspace():
            return False, "hash contains whitespace(s)"
    for hash_char in cleaned_hash:
        if hash_char in INVALID:
            return False, "hash contains invalid charater(s)"
    return True, ""
