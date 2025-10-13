
### extract_file_metadata
**Purpose:** Extract metadata from a file including name, size, type, extension, folder, and timestamps.

**Parameters:**  
- `file_path` (str): Path to the file.

**Returns:**  
- `dict`: Metadata including name, size, type, extension, folder, created, modified.

**Raises:**  
- `FileNotFoundError`: If the file does not exist.


----------------------------------------------------------

### validate_metadata_fields
**Purpose:** Ensure all required metadata fields exist and are not empty.

**Parameters:**  
- `metadata` (dict)  
- `required_fields` (list of str)

**Returns:**  
- `bool`: True if all required fields are present and not empty, False otherwise.


----------------------------------------------------------
### calculate_file_checksum
**Purpose:** Generate a checksum for a file using a specified algorithm for integrity verification or duplicate detection.

**Parameters:**  
- `file_path` (str)  
- `algorithm` (str, optional): "md5", "sha1", or "sha256" (default `"sha256"`)

**Returns:**  
- `str`: Hexadecimal hash of the file.

**Raises:**  
- `ValueError`: If the algorithm is unsupported.


----------------------------------------------------------

### rename_file_with_id
**Purpose:** Rename a file to include a unique ID before its extension.

**Parameters:**  
- `file_path` (str)  
- `unique_id` (str)

**Returns:**  
- `str`: New file path.


----------------------------------------------------------

### list_files_by_type
**Purpose:** List all files of a specific type in a directory and subdirectories.

**Parameters:**  
- `directory` (str)  
- `file_type` (str): File extension (e.g., ".pdf")

**Returns:**  
- `list of str`: Paths of matching files.


----------------------------------------------------------

## COMPLEX FUNCTIONS (30+ lines)

### organize_files_by_metadata
**Purpose:** Organize files (including subfolders) based on a specified metadata field.

**Parameters:**  
- `directory` (str)  
- `metadata_field` (str)

**Returns:**  
- None

**Raises:**  
- `FileNotFoundError`: If a file does not exist.


----------------------------------------------------------

### generate_archive_report
**Purpose:** Generate a detailed archive report including file count, total size, file types, month created, and top 5 largest files.

**Parameters:**  
- `directory` (str)  
- `output_path` (str)

**Returns:**  
- None


----------------------------------------------------------

### detect_duplicate_files
**Purpose:** Detect duplicate files in a directory using checksums; optionally remove duplicates.

**Parameters:**  
- `directory` (str)  
- `remove_duplicates` (bool, optional, default False)

**Returns:**  
- `list of tuples`: Each tuple contains paths of duplicate files.
