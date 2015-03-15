__author__ = 'Soheil'
from ping import ping, PingResult
import sys


def hosts_from_file(file_path):
    ofile = open(file_path)
    return ofile.readlines()


def run_multiple_pings(hosts):
    results = []
    for host in hosts:
        alias = None
        try:
            address, alias = host.strip().split()
        except Exception as exc:
            address = host.strip()
        result = ping(address, alias, 6)
        results.append(result)
        print(result)


def start_program():
    number_of_args = len(sys.argv)
    if number_of_args == 1:
        path = raw_input('Insert file path: ')
        array_of_hosts = hosts_from_file(path)
        run_multiple_pings(array_of_hosts)

    elif number_of_args == 2:
        array_of_hosts = hosts_from_file(sys.argv[1])
        run_multiple_pings(array_of_hosts)
    elif number_of_args > 2:
        print('Too many arguments given, only one hosts file address is excepted.')

if __name__ == '__main__':
    command = 's'
    while not command == 'n' and not command == 'q':
        start_program()
        command = raw_input('\nWanna retry? ')
        print('\n###############################################################################\n')