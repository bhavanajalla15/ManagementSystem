from passlib.hash import pbkdf2_sha256

def password_hasher(password):
    return pbkdf2_sha256.hash(password)

def check_password(password,hash):
    return pbkdf2_sha256.verify(password, hash)

# my_password= password_hasher("Bhavana@123")
# print(chech_password('Bhavana@123',my_password))