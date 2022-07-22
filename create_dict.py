import argparse
from os.path import exists


parser = argparse.ArgumentParser(description='Create dictionary from user and password file')
parser.add_argument('--user', '-u', dest='user', help='Users file', required=True)
parser.add_argument('--password', '-p', dest='password', help='Passwords file', required=True)
parser.add_argument('--output', '-o', dest='output', help='Output file', required=True)
args = parser.parse_args()

user_path = args.user
pass_path = args.password
output_path = args.output

if not exists(user_path):
    print(f'File {user_path} does not exist.')

if not exists(pass_path):
    print(f'File {pass_path} does not exist.')


user_list = open(user_path, 'r').read().split('\n')
pass_list = open(pass_path, 'r').read().split('\n')
output_file = open(output_path, 'w')

buffer = ""

for user in user_list:
    for password in pass_list:
        buffer += f'{user}:{password}\n'

output_file.write(buffer[:-1])
