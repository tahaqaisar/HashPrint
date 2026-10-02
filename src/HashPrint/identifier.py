# In the Name of God, the Most Compassionate, Most Merciful


from HashPrint.database import HASH_DATA, PASSWORD_HASH_DATA
import re


def is_hex_encoded(candidate_hash):
    hex_regex = re.compile(r"^[a-fA-F0-9]+$")
    if hex_regex.fullmatch(candidate_hash):
        return True
    return False


def identify(candidate_hash):
    possible_matches = []
    if is_hex_encoded(candidate_hash):
        for HASH_INFO in HASH_DATA:
            if HASH_INFO.pattern.fullmatch(candidate_hash):
                possible_matches.append(HASH_INFO)
    else:
        for PASSWORD_HASH_INFO in PASSWORD_HASH_DATA:
            if PASSWORD_HASH_INFO.pattern.fullmatch(candidate_hash):
                possible_matches.append(PASSWORD_HASH_INFO)
    return sorted(
        possible_matches, key=lambda matches: matches.popularity, reverse=True
    )
