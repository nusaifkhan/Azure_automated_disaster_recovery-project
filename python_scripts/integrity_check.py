import hashlib

def calculate_checksum(file_path):
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def verify_integrity(original, backup):
    original_checksum = calculate_checksum(original)
    backup_checksum = calculate_checksum(backup)
    if original_checksum == backup_checksum:
        print("Backup integrity verified!")
    else:
        print("Backup integrity failed!")

verify_integrity("/path/to/original/file", "/path/to/backup/file")
