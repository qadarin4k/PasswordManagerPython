from cryptography.fernet import Fernet
import os

KEY = "passwords.key" # This creates a file ending with key because we are storing something sensitive

if not os.path.exists(KEY):
    key = Fernet.generate_key() # this generates a random key
    with open(KEY, "wb") as KEY_FILE: # this opens the password file and writes binary
        KEY_FILE.write(key) # this writes the binary key in the file
    print("Encryption key generated") # notifies the user that the the key has been generated and saved in the file
else:
    with open(KEY, "rb") as KEY_FILE: # reads the key instead of creating a new one
        key = KEY_FILE.read()
fernet = Fernet(key) # create an object/variable for the key

Passwords = "passwords.txt" # creates a file to store all the passwords
if not os.path.exists(Passwords): # if the file doesn't exist, it will create one
    open(Passwords, "w").close()

def add_password(): # this will retrieve users account and password
    account = input("Enter account name: ")
    password = input("Enter password: ")
    encrypted = fernet.encrypt(password.encode())

    with open(Passwords, "a") as f: # this will add the inputed account and encrypted password with a separation and a line break in the password file
        f.write(f"{account} | {encrypted.decode()}\n") # this is using an f string

    print(f"Password for '{account}' saved!\n") # this will tell the user that the account has been succesfully been saved

def retrieve_password(): # this will reterive the account we are looking for
    account_to_find = input("Enter account to retrieve: ")

    with open(Passwords, "r") as f: # this will categorize the account and the encrypted password inn separate groups
        for line in f:
            account, encrypted = line.strip().split(" | ")

            if account == account_to_find: # if the account they are looking for is in the file, it will decrypt the password and return it
                decrypted = fernet.decrypt(encrypted.encode()).decode()
                print(f"Password for '{account}': {decrypted}\n")
                return
    print("Account not found.\n") # if not then it will notify the user

def list_accounts():
    print("Stored accounts:")
    with open(Passwords, "r") as f: # it will get the account side of the line and print it
        for line in f:
            account, _ = line.strip().split(" | ")
            print("-", account)
    print()

while True: # this the menu
    print("===== Password Manager =====")
    print("1. Add Password")
    print("2. Retrieve Password")
    print("3. List Accounts")
    print("4. Exit")

    choice = input("Select an option by picking the corresponding number: ")
    if choice == "1":
        add_password()
    elif choice == "2":
        retrieve_password()
    elif choice == "3":
        list_accounts()
    elif choice == "4":
        print("Exiting")
        break
    else:
        print("Invalid choice, try again.\n")
