import os
import sys
import argparse
import virustotal3.core
import virustotal3.enterprise

# https://chase-seibert.github.io/blog/2014/03/21/python-multilevel-argparse.html

if 'VT_API' in os.environ:
    api_key = os.environ['VT_API']

elif 'VT_API' not in os.environ:
    print('No VT_API environment variable found.')
    print('Please set the VT_API environment variable with your API key or use the --apikey argument.')

class virustotal(object):

    def __init__(self):
        parser = argparse.ArgumentParser(description='to complete',usage='virustotal <action> [<args>]')
        args = parser.add_argument('action', help='Action to execute')
        args = parser.parse_args(sys.argv[1:2])
        if not hasattr(self, args.action):
            print('Unknown action')
            parser.print_help()
            exit(1)
        getattr(self, args.action)()

    def domain(self):
        vt = virustotal3.core.Domains(api_key)
        parser = argparse.ArgumentParser(description='')
        parser.add_argument('domain', metavar='domain', action='store')
        parser.add_argument('option', metavar='opt', action='store')
        args = parser.parse_args(sys.argv[2:])

        d = args.domain
        option = args.option
        result = vt.get_relationship(d, option)
        print(result)


if __name__ == '__main__':

    virustotal()