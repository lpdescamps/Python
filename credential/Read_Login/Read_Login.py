# -*- coding: utf-8 -*-
from cryptography.fernet import Fernet
from pathlib import Path

REGION = 'EO'
PLATFORM = 'CUCM'
ROLE = 'rwx'
PATH = Path('C:\shared\API\credentials')

username = PATH / REGION / PLATFORM / ('user_' + ROLE + '.txt')
keyhash = PATH / REGION / PLATFORM / ('key_' + ROLE + '.txt')
hash = PATH / REGION / PLATFORM / ('hash_' + ROLE + '.txt')
server = PATH / REGION / PLATFORM / ('fqdn' + '.txt')


def crypto(keyhash, hash):
    with open(keyhash, 'rb') as file_key:
        for line_key in file_key:
            key = line_key
            cipher_suite = Fernet(key)
            with open(hash, 'rb') as file_hash:
                for line_hash in file_hash:
                    encryptedpwd = line_hash
                    uncipher_text = (cipher_suite.decrypt(encryptedpwd))
                    pwd = bytes(uncipher_text).decode("utf-8")
                    return pwd


def read(file):
    datalist = []
    for line in open(file):
        data = line.strip('\n')
        datalist.append(data)
    return datalist


def main():
    print(read(username)[0])
    print(crypto(keyhash, hash))
    print(read(server)[0])


if __name__ == '__main__':
    main()
