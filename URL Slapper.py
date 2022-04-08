from urllib import request, parse, error
from itertools import combinations_with_replacement as combinations
import string
import argparse
import tldextract
# Constants
alphanumerics = string.ascii_lowercase + string.digits
# Parse Arguments
parser = argparse.ArgumentParser()
parser.add_argument('domain', nargs='?', default="https://www.google.com", help='The domain format. Example: "https://www.google.com"')
args = parser.parse_args()
# URL Mangling
baseURL = tldextract.extract(args.domain)
print(baseURL)
url = baseURL
# Search Subdomains
for thing in combinations(alphanumerics, 3):
    try:
        url. = "".join(thing)
        response = request.urlopen('.'.join(part for part in url if part))
        
    except error.HTTPError as err:
        if err.code == 404:
            a = 1
        else:
            raise err
