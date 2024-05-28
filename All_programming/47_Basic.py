# Generate HashCode for files

import hashlib

def hash_file(filename):
    h = hashlib.sha1()

    with open(filename,'rb') as file:
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            h.update(chunk)
    return h.hexdigest()

result = hash_file(r"All_programming\body.txt")
print(result)