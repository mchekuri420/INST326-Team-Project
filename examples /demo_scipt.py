from src.library_name import (
    extract_file_metadata,
    validate_metadata_fields,
    calculate_file_checksum,
    rename_file_with_id,
    list_files_by_type,
    organize_files_by_metadata,
    generate_archive_report,
    detect_duplicate_files
)





# MEDIUM FUNCTIONS

# Extract metadata from a file
metadata = extract_file_metadata("demo_files/report.pdf")
print("Metadata:", metadata)

# Validate required metadata fields
required_fields = ["name", "size", "type", "created"]
if validate_metadata_fields(metadata, required_fields):
    print("All required metadata fields are present!")
else:
    print("Some metadata fields are missing or empty.")

# Calculate checksums for the file
checksum_md5 = calculate_file_checksum("demo_files/report.pdf", "md5")
checksum_sha256 = calculate_file_checksum("demo_files/report.pdf", "sha256")
print(f"MD5: {checksum_md5}")
print(f"SHA256: {checksum_sha256}")

# Rename the file with a unique ID
new_file_path = rename_file_with_id("demo_files/report.pdf", "DOC-123")
print(f"File renamed to: {new_file_path}")

# List all PDF files in the folder
pdf_files = list_files_by_type("demo_files", ".pdf")
print(f"Found PDF files: {pdf_files}")





# COMPLEX FUNCTIONS


# Organize files by metadata (type)
organize_files_by_metadata("demo_files", "type")
print("Files have been organized by type into subfolders.")

# Generate an archive report
output_report = "demo_files/archive_report.txt"
generate_archive_report("demo_files", output_report)
print(f"Archive report generated at: {output_report}")

# Detect duplicate files
duplicates = detect_duplicate_files("demo_files")
if duplicates:
    print("Duplicate files detected:")
    for dup1, dup2 in duplicates:
        print(f"  {dup1} and {dup2}")
else:
    print("No duplicate files found.")
