# Read Login Credential - User guide
You will need to edit Read_login.py REGION, PLATFORM, ROLE and PATH variable.

## Dependencies
>cryptography module

## Read_login.py
>Details explaining each variables
* **REGION**: Where your system is located. The region will help to build the folder structure. it could be for example:
  * EU
  * GB
* **PLATFORM**: What system you will be log in. The platform will help to build the folder structure. It could be for example:
  * Windows
  * Linux
  * SQL
* **ROLE**: The permission of your account. The role will help to build the filename. It could be for example:
  * r for read
  * rw for read and write
  * rwx for read, write and execute
* **PATH**: Where you want to store the credential files 
