# Password Manager in Python

This is a simple Python password manager project. It securely stores passwords using encryption.

---

## Encryption Key
- The key is stored in a file called `passwords.key` and it ends with `.key` because we are storing something sensitive.
- If the key file does not exist, a random key will be generated and saved.
- If the key file already exists, it will be read instead of creating a new one to avoid losing access to previous passwords.

---

## Password Storage
- Passwords are stored in a file called `passwords.txt`.
- If the file doesn't exist, it will be created automatically.

---

## Features / Functions

### Add Password
- This will retrieve the user's account and password.
- The password is encrypted using the key and saved to the password file.
- The account and encrypted password are separated by ` | ` and a new line is added.
- There will be text printed to notify the user that the account has been successfully saved.

### Retrieve Password
- This will retrieve the account the user is looking for.
- Opens the password file and separates each line into account and encrypted password.
- If the account is found, it will decrypts the password and displays it.
- If not found, it will notify the user.

### List Accounts
- Prints all stored accounts by reading the account side of each line in the password file.

---

## How to Run
1. Make sure Python is installed on your computer.
2. Install the cryptography library
  
