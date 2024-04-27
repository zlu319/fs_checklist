#!/usr/bin/env python3
# @author zlu319
# @version 0.1, 2024-4-20
"""
Copyright (c) 2024 zlu319

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""


import os  # filesystem traversal
import sys  # parse command line arguments
import csv  # to write output
import time # timestamp for error log
from typing import List, Union


def scan_and_report(src_dir_path: Union[str, bytes, os.PathLike], output_file_path: Union[str, bytes, os.PathLike], additional_columns: List):
    """
    Scans src_dir_path for files and writes each file to csv file specified by output_file_path, adding extra columns according to the columns parameter
    
    The output csv file will have the following format
    [FileName, AdditionalCol1, AdditionalCol2, ..., AdditionalColN, source_dir, subdir1, subdir2, ..., subdirN, FileName]
    Where "source_dir, subdir1, subdir2, ..., subdirN, FileName" basically form the path to the file, breadcrumbs style
    Note that the FileName is placed at the first column for readability purposes; as the path can be of variable length
    """
    csvlinestack = ["File Name"] + additional_columns + ["Path Breadcrumbs"]  # this is the first line in the csv file, specifying columns
    with open(output_file_path, 'w+') as report_csv_file:
        report_writer = csv.writer(report_csv_file)
        report_writer.writerow(csvlinestack)
        for root, _dir, files in os.walk(src_dir_path):
            splitroot = os.path.normpath(root).split(os.path.sep)  # on Unix, the first element of splitroot is 0
            # On Windows, the first element of splitroot is the drive letter
            # print(splitroot)
            csvlinestack =  [f"{splitroot[-1]}/"] + [""] * len(additional_columns) + splitroot + [os.sep]  # writes the directory name once
            report_writer.writerow(csvlinestack)
            for f in files:
                csvlinestack = [f] + [""] * len(additional_columns) + splitroot + [f] # writes all files in the directory
                report_writer.writerow(csvlinestack)


    


def cli_main():
    if len(sys.argv) < 3:
        print(f"Usage:\n{sys.argv[0]} <directory_path_to_scan> <path_to_output_file> <optional: additional columns for the checklist>")
    else:
        sdp = sys.argv[1]
        ofn = sys.argv[2]
        
        src_dir_path = os.path.normpath(sdp)
        output_filename = os.path.normpath(ofn)
        
        additional_columns = sys.argv[3:]
        
        if not os.path.exists(src_dir_path):
            print("Error: source directory does not exist!")
            return

        if os.path.exists(output_filename):
            c = input("Output File Already Exists. Overwrite? [y, N]")
            if c.lower() != 'y':
                print("Output File not overwritten, scan cancelled. Please specify other filename.")
                return
        
        scan_and_report(src_dir_path, output_filename, additional_columns)
        

# function to write a log file; not used so far; primarily intended for debugging
def _create_log():
    program_directory = os.getcwd()  # current working directory used by this python program
    log_dir_path = os.path.join(program_directory, "log")
    if not os.path.exists(log_dir_path):
        os.makedirs(log_dir_path)  # creates a log folder wthin the program directory if one does not exist already
    log_path = os.path.join(out_dir_path, f"error_log_{int(time.time())}.txt")
    with open(log_path, 'w+') as log_file:
        log_file.writelines(f"Log Begins on timestamp {int(time.time())}")



if __name__ == '__main__':
    cli_main()  # the main function for the book censor
