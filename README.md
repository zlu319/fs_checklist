# Filesystem Checklist Generator

Author: zlu319

*Version 1.0, Created on Apr 20, 2024*

*Licensed under the MIT License*

The program walks through all files and subdirectories of a specified directory in  a filesystem and generates a checklist with user-specified columns in the form of a CSV file. One may then open the CSV file with their spreadsheet editor of choice, such as LibreOffice Calc or Microsoft Excel.

The output csv file will have the following format
```
    [FileName, AdditionalCol1, AdditionalCol2, ..., AdditionalColN, source_dir, subdir1, subdir2, ..., subdirN, FileName]
    Where "source_dir, subdir1, subdir2, ..., subdirN, FileName" basically form the path to the file, breadcrumbs style
    Note that the FileName is placed at the first column for readability purposes; as the path can be of variable length
```

## Architecture Documentation

The source code is located in the `src/` folder. It consists of the following file
* `main.py` - containing the primary logic for the program

Files for testing are located in the `test/` folder,:
* `dir1/` a sample directory for testing, created on macOS
* `os_walk_tester.py` a small utility script to test the os.walk() function in Python

## Dependencies and Platforms

* Tested on macOS 11.7.10 Big Sur
* Python >= v3.6 (v3.8.9 tested)

