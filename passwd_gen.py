import string
import secrets

def gen_passwd():
    length = int(input('Introduce the passwd_length: '))
    char = string.digits + string.ascii_lowercase + string.ascii_uppercase + string.punctuation
    password = "".join(secrets.choice(char) for i in range(length))
    print(password)

if __name__ == "__main__":
    gen_passwd()
