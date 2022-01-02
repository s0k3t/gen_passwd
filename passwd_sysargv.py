import secrets
import string
import sys
from termcolor import cprint


if len(sys.argv) <= 1:
    cprint("Place an integer representing the password's length desired.", "green")
    cprint("Example: python3 passwd.py 19", "yellow")
    exit(0)
else:
    num = int(sys.argv[1])
    char = string.digits + string.ascii_lowercase + string.ascii_uppercase + string.punctuation
    passwd = "".join(secrets.choice(char)for i in range(num))
    print(passwd)



