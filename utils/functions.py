from hashlib import sha256


def sha_encode(hash_string):
    # Encodes a string with SHA256 encoding
    sha = sha256(hash_string.encode()).hexdigest()[:15]
    return sha
