# Let's create a pasword encryption program

import base64

def encrypt_pass(password):
    encoded_bytes = base64.b64encode(password.encode())
    print(encoded_bytes)

# user_pass = input("Enter your password: ")
# encrypt_pass(user_pass)


# def decrypt_pass(password):
#     decoded_bytes = base64.b64decode(password)
#     decoded_data = decoded_bytes.decode()
#     print(f"The password is: {decoded_data}")

def decrypt_pass(password):
    decoded_byes = base64.standard_b64decode(password)
    decoded_data = decoded_byes.decode()
    print(decoded_data)

user_pass = input("Enter your decoded password: ")
decrypt_pass(user_pass)
