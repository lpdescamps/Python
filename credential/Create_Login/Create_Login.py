from cryptography.fernet import Fernet
from pathlib import Path
import csv

FILE = Path('C:\shared\API\credentials\info.csv')


def readCSV(file):
    for row in csv.DictReader(open(file)):
        yield row


def crypto(login):
    path = Path(login['path'] + '\\' + login['region'] + '\\' + login['platform'])
    path.mkdir(parents=True, exist_ok=True)
    pwd = login['password']

#   Create the Symmetric Key
    key = Fernet.generate_key()

#   Create the Hash for PWD and write files
    cipher_suite = Fernet(key)
    ciphered_text = cipher_suite.encrypt(pwd.encode())
    with open(path / 'fqdn.txt', 'w') as f: f.write(login['server'])
    with open(path / ('key_' + login['role'] + '.txt'), 'wb') as f: f.write(key)
    with open(path / ('user_' + login['role'] + '.txt'), 'w') as f: f.write(login['username'])
    with open(path / ('hash_' + login['role'] + '.txt'), 'wb') as f: f.write(ciphered_text)


def main():
    for login in readCSV(FILE):
        crypto(login)


if __name__ == '__main__':
    main()