import os
import platform
import sys
from typing import Dict, List
import py7zr

def get_slashtype() -> str:
    if platform.architecture()[1] == "WindowsPE":
        return '\\'
    else:
        return '/'

def get_name(fullpath: str) -> str:
    path = os.path.abspath(fullpath)
    return path.split(get_slashtype())[-1]

def get_full_path(fullpath: str) -> str:
    path = os.path.abspath(fullpath)
    return path.split(get_slashtype())

# using list comprehension
def archive_files(outPath: str, targetFolder: str, excludeFile = None) -> str:
    try:
        targetFolderName = get_name(targetFolder)
        files = []
        
        if (excludeFile != None):
            print("Exclude file provided")
            excludeList = open(excludeFile, 'r', encoding='utf-8').read().split('\n')
            files = [
                os.path.join(root, name)
                for root, dirs, files in os.walk(targetFolder)
                for name in files
                if name not in excludeList
            ]
        else:
            print("No exclude file provided")
            files = [
                os.path.join(root, name)
                for root, dirs, files in os.walk(targetFolder)
                for name in files
            ]
            
        with py7zr.SevenZipFile(f"{outPath}", mode='w') as out:
            for file in files:
                path = get_full_path(file)
                indexum = int(path.index(targetFolderName))
                out.write(file, get_slashtype().join(path[indexum:]))
                
        
        return 0
    except Exception as e:
        print(e)
        return 1

## full path required.
if __name__ == "__main__":
    args = sys.argv
    if len(args) <= 2:
        print("[-] No inputs given. Exiting.")
        print(
            '[!] Usage  : $ python archiver.py [outPath] [targetFolder], [excludeFile]\n' +
            '[!] Example: $ python archiver.py "test.7z" "C:\\files" "exclude.txt"'
        )
        sys.exit(1)
    else:
        outPath = args[1]
        path = args[2]
        status = None
        if len(args) > 3:
            excludeFile = args[3]
            status = archive_files(outPath=outPath, targetFolder=path, excludeFile=excludeFile)
        else:
            status = archive_files(outPath=outPath, targetFolder=path)
        
        if (status == 0):
            print("[+] Done!")
            sys.exit(0)
        else:
            print("[-] Failed!")
            sys.exit(1)
