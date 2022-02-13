Simple File archiver with py7zr module.

- You can also exclude files with a specified text file.
- Note that this preliminary version only uses the default py7zr compression values.

# Requirements
* py7zr

# Installation
```
pip install -r requirements.txt
```

# Usage
```
$ python archiver.py [outPath] [targetFolder], [excludeFile]
```

# Example
```
$ python archiver.py "test.7z" "C:\files" "exclude.txt"
```