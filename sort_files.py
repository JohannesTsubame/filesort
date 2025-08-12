#!/usr/bin/env python3

import os
import shutil


def main():   
    base_dir = "./"

    file_types = {
        'images': ['.jpg', '.jpeg', '.png', '.gif'],
        'documents': ['.pdf', '.docx', '.doc', '.txt', ".xls", ".ppt", '.pptx'],
        "spreadsheets": [".xls", '.xlsx', '.csv'],
        'audio': ['.mp3', '.wav', '.aac'],
        'video': ['.mp4', '.avi', '.mov'],
        'archives': ['.zip', '.rar', '.tar', '.gz'],
        'code': ['.py', '.ipynb' , '.js', '.html', '.css', '.java', '.cpp'],
        'others': []}

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
