import argparse
import secrets
import string

my_parser = argparse.ArgumentParser(description="Password generator")
my_parser.add_argument('--int',
                        type=int, 
                        help='add an int, default:19', 
                        default=19)
args = my_parser.parse_args()

num = args.int
char = string.digits + string.ascii_lowercase + string.ascii_uppercase + string.punctuation
password = "".join(secrets.choice(char) for i in range(num))
print(password)
