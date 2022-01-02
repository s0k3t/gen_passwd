import secrets
import string
import sys

def passwd(num):
    length = num
    char = string.digits + string.ascii_lowercase + string.ascii_uppercase + string.punctuation
    password = "".join(secrets.choice(char) for i in range(length))
    return password


def gen():
    yield passwd(19)

groups = ['Bob', 'Peter', 'Bunny', 'Rita', 'Judy', 'Marcia']

with open('/path/to/filename.csv', 'a') as f:
    sys.stdout = f

    for singer in groups:
        print(f"{singer},", next(gen()))
    sys.stdout
    f.close()

