"""
library_name.py — Digital Archive Management Utility Library

A collection of simple, intermediate-level functions to help organize, 
manage, and retrieve digital files for academic and collaborative projects.
"""

import os
import shutil
import mimetypes
import uuid
from datetime import datetime




############ SIMPLE FUNCTIONS (7) ##############















########### MEDIUM FUNCTIONS (5) ##############


def extract_file_metadata(file_path):
    """
    Get basic metadata about a file.
    
    Args:
        file_path (str): Path to the file.
        
    Returns:
        dict: Metadata such as their name, size, type, when created, and when modified.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"{file_path} not found.")
    
    stat = os.stat(file_path)
    metadata = {
        "name": os.path.basename(file_path),
        "size": format_file_size(stat.st_size),
        "type": mimetypes.guess_type(file_path)[0] or "unknown",
        "created": datetime.fromtimestamp(stat.st_ctime).strftime("%Y-%m-%d %H:%M:%S"),
        "modified": datetime.fromtimestamp(stat.st_mtime).strftime("%Y-%m-%d %H:%M:%S")
    }
    return metadata



def validate_metadata_fields(metadata, required_fields):
    """
    Check that required fields exist and are not empty.
    
    Args:
        metadata (dict): Metadata dictionary.
        required_fields (list): List of required keys.
        
    Returns:
        bool: If all required fields exist its True .
    """
    for field in required_fields:
        if field not in metadata or not metadata[field]:
            return False
    return True



def calculate_file_checksum(file_path, algorithm="sha256"):
    """
    Calculate a file hash for duplicates or verification.
    
    Args:
        file_path (str): File to hash.
        algorithm (str): Hash type ('md5', 'sha1', 'sha256').
        
    Returns:
        str: Hex digest of hash.
    """
    import hashlib
    if algorithm not in ["md5", "sha1", "sha256"]:
        raise ValueError("Unsupported hash type.")
    
    hash_func = getattr(hashlib, algorithm)()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_func.update(chunk)
    return hash_func.hexdigest()



def rename_file_with_id(file_path, unique_id):
    """
    Rename a file to include a unique identifier.
    
    Args:
        file_path (str): Path to the file.
        unique_id (str): Unique ID string.
        
    Returns:
        str: New file path.
    """
    directory, filename = os.path.split(file_path)
    name, ext = os.path.splitext(filename)
    new_name = f"{sanitize_filename(name)}_{unique_id}{ext}"
    new_path = os.path.join(directory, new_name)
    os.rename(file_path, new_path)
    return new_path



def list_files_by_type(directory, file_type):
    """
    List all files of a given type in a directory.
    
    Args:
        directory (str): Directory path.
        file_type (str): File extension (e.g., '.pdf').
        
    Returns:
        list: List of file paths.
    """
    return [os.path.join(directory, f) for f in os.listdir(directory)
            if f.lower().endswith(file_type.lower())]



################ COMPLEX FUNCTIONS (3) ##################


def organize_files_by_metadata(directory, metadata_field):
    """
    Organize files in a directory into subfolders based on a specific metadata field.

    Args:
        directory (str): Path to the directory containing files.
        metadata_field (str): The metadata field to use for folder grouping 
                              (e.g., 'type', 'created', 'modified').

    Raises:
        FileNotFoundError: If a file in the directory does not exist.

    Example:
        organize_files_by_metadata("/home/user/docs", "type")
        # Moves PDF files into /home/user/docs/pdf, images into /home/user/docs/jpeg, etc.
    """
    for f in os.listdir(directory):
        path = os.path.join(directory, f)
        if os.path.isfile(path):
            meta = extract_file_metadata(path)
            field_value = meta.get(metadata_field, "Unknown")
            folder = os.path.join(directory, str(field_value).replace(" ", "_"))
            if not os.path.exists(folder):
                os.makedirs(folder)
            shutil.move(path, os.path.join(folder, f))















