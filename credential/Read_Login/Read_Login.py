# -*- coding: utf-8 -*-
from cryptography.fernet import Fernet
from pathlib import Path

REGION = 'EO'
PLATFORM = 'CUCM'
ROLE = 'rwx'
PATH = Path('C:\shared\API\credentials')

server = PATH / REGION / PLATFORM / ('fqdn' + '.txt')


def file(role):
    username = PATH / REGION / PLATFORM / ('user_' + role + '.txt')
    keyhash = PATH / REGION / PLATFORM / ('key_' + role + '.txt')
    hash = PATH / REGION / PLATFORM / ('hash_' + role + '.txt')

    return username, keyhash, hash


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

    print('username:', read(file(ROLE)[0])[0])
    print('password:', crypto(file(ROLE)[1], file(ROLE)[2]))
    print('server:', read(server)[0])

if __name__ == '__main__':
    main()
