import string
import secrets

def passwd(num):
    length = num
    char = string.digits + string.ascii_lowercase + string.ascii_uppercase + string.punctuation
    password = "".join(secrets.choice(char) for i in range(length))
    return password
