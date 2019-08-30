import os
import argparse
import virustotal3.core
import virustotal3.enterprise

parser = argparse.ArgumentParser()
parser.add_argument('--apikey', action='store', help='Set a VirusTotal API key', required=False)
# https://chase-seibert.github.io/blog/2014/03/21/python-multilevel-argparse.html

args = parser.parse_args()

if 'VT_API' in os.environ:
    api_key = os.environ['VT_API']

elif ('VT_API' not in os.environ) and (args.apikey is None):
    print('No VT_API environment variable found.')
    print('Please set the VT_API environment variable with your API key or use the --apikey argument.')

if args.apikey:
    api_key = args.apikey




