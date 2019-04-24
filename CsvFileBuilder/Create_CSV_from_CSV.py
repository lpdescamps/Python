# -*- coding: utf-8 -*-
import csv
from pathlib import Path, PurePath

##Source CSV file
READ_FILE = Path("C:\\Users\louis\Downloads\\tms\\All.csv")

##Folder location for the new files
FILE = "C:\\Users\louis\Downloads\\tms\\files\\"


def dictread(file):
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            yield row
def read(file):
    with open(file) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            yield row
def read_h(file):
    with open(file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader, None)
        yield headers[1:]
def dictwrite_h(file,headers):
    with open(file, 'w', newline='') as csvfile:
        fieldnames = headers
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
def write_csv(file,*args):
    with open(file, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_NONE, delimiter="\t")
        writer.writerow(args)

def main():
    p = Path(FILE).glob('**/*')

    for item in dictread(READ_FILE):
        for header in read_h(READ_FILE):
            dictwrite_h(Path(FILE + item['CSV_file'] + '.csv'), header)

    for file in p:
        for item in read(READ_FILE):
            if item[0] == PurePath(str(file)).stem:
                line = ",".join(item[1:])
                write_csv(str(file), line)

if __name__ == '__main__':
    main()