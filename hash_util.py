import hashlib as hl
import json


def hash_string_256(string):
    return hl.sha256(string).hexdigest()


def hash_block(block):
    """ Create an SHA-256 hash of a Block """
    return hash_string_256(json.dumps(block, sort_keys=True).encode())
