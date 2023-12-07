#!/usr/bin/env python
# coding: utf-8

# # Python password generator

# In[2]:


import random
import string

def generate_password(length=12):
    # Define character sets
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    # Combine all character sets
    all_chars = lowercase_letters + uppercase_letters + digits + special_chars

    # Generate password
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

def generate_multiple_passwords(num_passwords, length=12):
    passwords = [generate_password(length) for _ in range(num_passwords)]
    return passwords

if __name__ == "__main__":
    print("Welcome to the Strong Password Generator!")
    print("This tool creates secure passwords with a mix of uppercase and lowercase letters, numbers, and special characters.")

    while True:
        try:
            num_passwords = int(input("Enter the number of passwords to generate: "))
            length = int(input("Enter the length of each password: "))
            break
        except ValueError:
            print("Please enter valid numbers.")

    passwords = generate_multiple_passwords(num_passwords, length)

    print("\nGenerated Passwords:")
    for idx, password in enumerate(passwords, start=1):
        print(f"Password {idx}: {password}")


# In[ ]:




