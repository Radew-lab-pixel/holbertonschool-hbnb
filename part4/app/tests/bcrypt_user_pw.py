import bcrypt

# Password to Hash
# my_password = b'Sachinfromgeekpython'
my_password = b'password'

# Generating Salt
salt = bcrypt.gensalt()

# Hashing Password
hash_password = bcrypt.hashpw(
    password=my_password,
    salt=salt
)

print(f"Actual Password: {my_password.decode('utf-8')}")
# Print Hashed Password
print(f"Hashed Password: {hash_password.decode('utf-8')}")