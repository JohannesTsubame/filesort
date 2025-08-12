#!/usr/bin/env python3

import os
import shutil


def main():   
    base_dir = "./"

    file_types = {
        'Images': [# Common Raster Formats
                   ".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".tif",

                   # Web & Modern Formats
                   ".webp", ".avif", ".heif", ".heic",

                   # Vector Formats
                   ".svg", ".eps", ".ai",

                   # RAW Camera Formats (common ones)
                   ".cr2", ".cr3", ".nef", ".arw", ".orf", ".rw2", ".dng"],
        'Documents': [# Text Documents
                      ".txt", ".rtf", ".odt", ".md",

                      # Microsoft Word & Similar
                      ".doc", ".docx", ".dot", ".dotx",

                      # PDFs & Other Read-Only Docs
                      ".pdf",

                      # eBooks
                      ".epub", ".mobi", ".azw3"],
        "Spreadsheets": [# Microsoft Excel
                        ".xls", ".xlsx", ".xlsm", ".xlsb", ".xlt", ".xltx", ".xltm",

                        # OpenDocument & LibreOffice
                        ".ods", ".ots",

                        # Comma/Tab Delimited
                        ".csv", ".tsv",

                        # Other spreadsheet formats
                        ".numbers"],
        'Presentations': [# Microsoft PowerPoint
                          ".ppt", ".pptx", ".pptm", ".pot", ".potx", ".potm",

                          # OpenDocument & LibreOffice
                          ".odp", ".otp",

                          # Other presentation formats
                          ".key"],
        'Audio': [# Common Compressed Formats
                  ".mp3", ".aac", ".ogg", ".wma", ".m4a",

                  # Uncompressed / Lossless Formats
                  ".wav", ".flac", ".alac", ".aiff", ".aif",

                  # Other / Less Common
                  ".opus", ".amr", ".mid", ".midi"],
        'Video': [# Common Formats
                  ".mp4", ".m4v", ".mov", ".avi", ".wmv", ".flv", ".mkv",

                  # Web & Streaming Formats
                  ".webm", ".ogv",

                  # Other / Less Common
                  ".3gp", ".3g2", ".mts", ".m2ts", ".ts", ".vob"],
        'Archives': [# Common Archive Formats
                     ".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz",

                     # Disk Image Formats
                     ".iso", ".img", ".dmg", ".vhd", ".vhdx",

                     # Other / Less Common
                     ".tgz", ".tbz2", ".lz", ".z"],
        'Code': [# Web Development
                ".html", ".htm",
                ".css",
                ".js", ".mjs", ".cjs",
                ".ts", ".tsx",
                ".php", ".phtml",
                ".rb",
                ".aspx", ".cshtml",

                # General-Purpose Programming
                ".py", ".pyw", ".ipynb",
                ".java",
                ".c", ".h",
                ".cpp", ".cc", ".cxx", ".hpp", ".hxx",
                ".cs",
                ".go",
                ".rs",
                ".kt", ".kts",
                ".swift",
                ".m", ".mm",

                # Scripting Languages
                ".sh",
                ".bash",
                ".ps1",
                ".pl", ".pm",
                ".lua",

                # Data Science / Analytics
                ".r", ".R",
                ".m",  # MATLAB
                ".jl",
                ".sas",

                # Markup & Configuration
                ".yml", ".yaml",
                ".json",
                ".xml",
                ".toml",
                ".ini",
                ".md"],
        'Others': []}

    #if Dir does not exist
    def mkdir(base_dir, directories):
        for dir in directories:
            path = os.path.join(base_dir, dir)
            if not os.path.exists(path):
                os.makedirs(path)

    def sort_files(base_dir, file_types):
        for file in os.listdir(base_dir):
            path = os.path.join(base_dir, file)

            # Skip directories
            if os.path.isdir(path):
                continue
            
            # Skip hidden files
            if file.startswith('.'):
                continue
                
            # Check file extension
            file_ext = os.path.splitext(file)[1].lower()

            #Move file to the appropriate directory
            moved = False
            for dir_name, extensions in file_types.items():
                if file_ext in extensions:
                    target_dir = os.path.join(base_dir, dir_name)
                    shutil.move(path, target_dir)
                    moved = True
                    break
            
            # If it doesn't match any category, move it to "others"
            if not moved:
                target_dir = os.path.join(base_dir, 'others')
                shutil.move(path, target_dir)

            
    mkdir(base_dir, file_types.keys())
    sort_files(base_dir, file_types)

if __name__ == "__main__":
    main()
    print("Files Sorted")
